#sum of digits in 2^1000

digit_sum = 0
number = str(2**1000)
for x in number:
	digit_sum = digit_sum + int(x)
print digit_sum
