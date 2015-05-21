from math import sqrt
a = []
b = [2, 3]
for x in range(1, 1000000):
	if x % 2 == 1:
		a.append(x)
a.remove(1)
a.remove(3)

for x in a:
	c = 0
	while b[c] <= sqrt(x):
		if x % b[c] == 0:
			break
		else: c = c + 1
	else:
		b.append(x)
z = 0

for x in b:
	c = 0
	t = 0
	f = b.index(x)
	while t < 1000000:
		t += b[f]
		c += 1
		if t in b and c > z:
			z = c
			print t
			print z
		f += 1
