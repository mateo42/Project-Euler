# Things I reuse a lot when solving Project Euler problems
from math import sqrt

# Tells if a number is prime by trial division
def isPrime( num ):
	# xrange over all possible factors up to the square root
	for i in xrange( 2, int( sqrt( num ) ) +1 ) :
		# if it is a factor, then this number is not prime
		if ( num % i == 0 ):
			return False

	# no factors, we found a prime!
	return True

# yields primes from 2 to infinity
def primes():
	prime = 2
	while True:
		if( isPrime( prime) ):
			yield prime
		prime += 1