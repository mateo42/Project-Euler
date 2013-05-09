# Sum of primes below 2 million
from math import sqrt
from Euler import isPrime

print sum(filter(lamda x: isPrime(x), i for i in range(TWO_MILLION - 1, 1, -2)))