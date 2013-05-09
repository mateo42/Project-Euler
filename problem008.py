f = open('problem008.txt')
number = f.read()
largestProduct = 0

for i in range( len( number ) - 5 ):
	sum = 1
	for n in number[ i : (i+5) ]:
		sum *= int( n )

	if (sum > largestProduct):
		largestProduct = sum

print largestProduct