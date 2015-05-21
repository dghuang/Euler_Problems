#smallest positive number evenly divisible by numbers from 1 to 20
#increment by 9699690, which is the product of 11, 13, 14, 15, 17, 19
#which are the prime or products of primes between 11-20

number = 9699690

while not (number % 12 == 0 and number % 16 == 0 and number % 18 == 0 and number % 20 == 0):
	number += 9699690

print number