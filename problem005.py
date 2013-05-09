# smallest positive number that is evenly divisible by all of the numbers from 1 to 20

def multiplesOf20():
	'''Yield increasing multiples of 20'''
	i = 20
	while True:
		yield i
		i += 20

def divisibleByAll( number ):
	''' Checks that arguments is divisible by 3 - 19 '''
	# Skip 1, 2, 20
	for i in range(3,20):
		if ( (number % i) != 0):
			return False
	return True

def findSmallestDivisibleTo20():
	'''Loop over multiples of 20, find first one divisible by all numbers up to 20'''
	for i in multiplesOf20():
		if divisibleByAll( i ):
			return i

print findSmallestDivisibleTo20()