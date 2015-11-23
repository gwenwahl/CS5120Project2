#Standard Fibonacci

import resource
import sys
import datetime

sys.setrecursionlimit(99999)

def fib(x):
	if x == 0:
		return 0
	if x == 1:
		return 1
	return fib(x - 1) + fib(x - 2)



if __name__ == '__main__':
	start  = datetime.datetime.now()
	result = fib(int(sys.argv[1]))
	end    = datetime.datetime.now()

	delta = end - start

	print str(result) + ', ' + str(int((delta.total_seconds() * 1000000) + delta.microseconds))

