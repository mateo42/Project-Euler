# smallest positive number that is evenly divisible by all of the numbers from 1 to 20

# Yields infinitely increasing multiples of 20
def multiplesOf20():
	i = 20
	while True:
		yield i
		i += 20

# Checks that arguments is divisible by 3 - 19
def divisibleByAll( number ):
	# Skip 1, 2, 20
	for i in range(3,20):
		if ( (number % i) != 0):
			return False
	return True

# Loop over multiples of 20, find first one divisible by all numbers up to 20
def findSmallestDivisibleTo20():
	for i in multiplesOf20():
		if divisibleByAll( i ):
			return i

print findSmallestDivisibleTo20()