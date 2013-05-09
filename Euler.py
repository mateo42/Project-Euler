# Things I reuse a lot when solving Project Euler problems
from math import sqrt

def isPrime( num ):
	''' Test if a number is prime using trial division '''
	
	# xrange over all possible factors up to the square root
	for i in xrange( 2, int( sqrt( num ) ) +1 ) :
		# if it is a factor, then this number is not prime
		if ( num % i == 0 ):
			return False

	# no factors, we found a prime!
	return True

def primes():
	''' Yield primes from 2 to infinity '''
	prime = 2
	while True:
		if( isPrime( prime) ):
			yield prime
		prime += 1

def memoize( func, arg ):
	''' Save the result of a previous call '''

