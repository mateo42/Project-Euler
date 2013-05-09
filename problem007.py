# find 10001st prime number
from Euler import primes, isPrime

def findNthPrime( n ):
	i = 1
	for p in primes():
		if ( i == n ):
			return p
		i += 1
			
print findNthPrime( 10001 )



