#find the sum of all the digits in 100 factorial

def factorial(n):
	if n == 1:
		return 1
	return n*factorial(n-1)
	
number = factorial(100)
digit_sum = 0
for letter in str(number):
	digit_sum = digit_sum + int(letter)
print digit_sum