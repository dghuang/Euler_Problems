#collatz sequence: given a starting number, if it is even, divide by 2, if odd, 3n + 1
#if all collatz sequences end at 1 find the largest chain of numbers under a million

f = 0
for x in range (1, 1000000):
	r = 0
	z = x
	while z != 1:
		if z % 2 == 0 and z > 1:
			z = z / 2
			r = r + 1
		else:
			z = 3 * z + 1
			r = r + 1
	if r > f:
		f = r
		print x
