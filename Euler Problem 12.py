triangle_number = 3
term_number = 3
divisor_list = []
while len(divisor_list) < 501:
	del divisor_list[:]
	triangle_number = triangle_number + term_number
	z = 0
	r = 1
	if triangle_number % 2 == 0:
		while z <= (triangle_number / r):
			z = z + 1
			if triangle_number % z == 0:
				divisor_list.append(z)
				divisor_list.append(triangle_number/z)
				r = z
	term_number = term_number + 1

print triangle_number