#Bottom Up Fibonacci

import resource
import sys
import datetime

sys.setrecursionlimit(99999)

def fib(x):
	m = {'0' : 0, '1' : 1}
	for i in range(2, x + 1):
		m[str(i)] = m[str(i - 1)] + m[str(i - 2)]
	return m[str(x)]	

if __name__ == '__main__':
	start  = datetime.datetime.now()
	result = fib(int(sys.argv[1]))
	end    = datetime.datetime.now()

	delta = end - start

	print str(result) + ', ' + str(int((delta.total_seconds() * 1000000) + delta.microseconds))