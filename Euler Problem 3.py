#find largest prime factor of 600851475143

def isPrime(number):
	for n in range(2, int(number**0.5) +1):
		if (number % n == 0):
			return False
	return True

prime, highest_divisor = 600851475143, 0

for x in range(3, 775147, 2):
	if prime % x == 0 and isPrime(x) == True:
		highest_divisor = x

print highest_divisor