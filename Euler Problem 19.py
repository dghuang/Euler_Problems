r = 1901
b = 29
c = 0

while r != 2001:
	y = {1 : range(1,32),
	2 : range(1, 29),
	3 : range(1, 32),
	4 : range(1, 31),
	5 : range(1, 32),
	6 : range(1, 31),
	7 : range(1, 32),
	8 : range(1, 32),
	9 : range(1, 31),
	10 : range(1, 32),
	11 : range(1, 31),
	12 : range(1, 32),}
	if r % 4 == 0:
		y[2] = range(1, 30)
		for x in y:
			a = len(y[x]) % 7
			b = b + a
			if b % 7 == 6:
				c = c + 1
		r = r + 1
	else:
		for x in y:
			a = len(y[x]) % 7
			b = b + a
			if b % 7 == 6:
				c = c + 1
		r = r + 1

print c
