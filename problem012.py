# Fist triangle number with over 500 divisors
from math import sqrt

def triangleNumbers():
	i = 1
	triangle = 0

	while True:
		triangle += i
		i += 1
		yield triangle


def numFactorsOf(x):
	'''Up to the square root of x, take divisor i and complimentary factor x/i, reduce the two lists output
	   from the range function to one list, then conver the list to a set to remove duplicates, 
	   finally and take the length of that set... phew! '''
    return 	len(	
    			set(	
    				reduce(
    					list.__add__, 
    					([i, x/i] for i in range(1, int(sqrt(x)) + 1) if (x % i) == 0)
    				)
   				)
    		)

def findTriangleNumber():
	for t in triangleNumbers():
		if( numFactorsOf(t) > 500):
			return t

print findTriangleNumber()

