#Bottom Up Rod Cutting

import resource
import sys
import datetime

sys.setrecursionlimit(99999)

def cut_rod(prices, n):
	r = [0 for x in range(n+1)]
	s = [0 for x in range(n)]
	r[0] = 0
 
	for i in range(1, n+1):
		q = -999999
		for j in range(i):
			y = int(prices[j]) + r[i-j-1]
			if q < y:
				q = y
				s[i - 1] = j + 1
		r[i] = q
 
	return r, s

if __name__ == '__main__':

	p = []
	for i in range(1, len(sys.argv)):
		p.append(sys.argv[i])

	start  			 = datetime.datetime.now()
	r, s 			 = cut_rod(p, len(p))
	end    			 = datetime.datetime.now()

	delta = end - start
	print str(int((delta.total_seconds() * 1000000) + delta.microseconds))
	n = len(p)
	while n > 0:
		print s[n - 1]
		n = n-s[n - 1]