# Max palindrome that is the product of 3 digit numbers

MAX_3DIG_NUM = 999
MIN_3DIG_NUM = 100

def isPalindrome( integer ):
	return str(integer) == str(integer)[::-1]

def findMaxPalindrome():
	palindrome = 0
	for x in range( MAX_3DIG_NUM, MIN_3DIG_NUM/2 - 1, -1 ):
		for y in range( MAX_3DIG_NUM/2, MIN_3DIG_NUM - 1, -1 ):
			num = x * y
			if ( num > palindrome and isPalindrome( num ) ):
				palindrome = num

	return palindrome

p = findMaxPalindrome()
print "Max palindrome is %d" % p