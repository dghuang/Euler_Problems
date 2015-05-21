#if a pythagorean triplet is a^2 + b^2 = c^2
#find a*b*c such that a + b + c = 1000

list = []
for x in range(1, 1001):
	list.append(x**2)

for x in range(1, 1001):
	for y in range(1, 1001):
		sum_squares = x ** 2 + y ** 2
		if sum_squares in list and x + y + sum_squares**0.5 == 1000:
			print x * y * sum_squares ** 0.5