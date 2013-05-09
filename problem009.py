# find product of pythagorean triplet (a^2 + b^2 = c^2 where a < b < c) where a + b + c  = 1000
from math import sqrt

def pythagoreanTriplet():
	for a in range(500):
		for b in range(500):
			c = sqrt(a**2 + b**2)
			if ( ( (a + b + c) == 1000 ) and  (a < b < c) and ( (a**2) + (b**2) ) == (c**2) ):
				return (a, b, c)
					
(a, b, c) = pythagoreanTriplet()
print "(%d, %d, %d), %d"  % (a, b, c, (a * b * c) )