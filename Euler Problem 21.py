from math import sqrt
f = 0

a = range(1, 10001)
for x in a:
	c = 1
	b = []
	e = []
	while c < sqrt(x):
		if x % c == 0:
			b.append(c)
			if x/c != x:
				b.append(x/c)
		c += 1
	c = 1
	s = 0
	for g in b:
		s = s + g
	while c < sqrt(s):
		if s % c == 0:
			e.append(c)
			if s/c != s:
				e.append(s/c)
		c += 1
	q = 0
	for p in e:
		q += p
	if q == x:
		print x
		print s
		f = f + x
print f
