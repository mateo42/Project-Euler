# Largest prime factor of 600,851,475,143
from math import sqrt
from Euler import isPrime

theNumber = 600851475143

print max(filter(lambda x: isPrime(x), (i for i in xrange( int(sqrt(theNumber)), 2, -1) if theNumber % i == 0)))
