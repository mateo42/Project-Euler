# Difference between sum of squares of first 100 natural numbers and square of the sum

def sumOfSquares( number ):
	sum = 0
	for i in range( number +1 ):
		sum += i ** 2
	return sum

def squareOfSum( number ):
	sum = 0
	for i in range( number + 1 ):
		sum += i

	return sum ** 2

print abs(sumOfSquares( 100 ) - squareOfSum( 100 ))