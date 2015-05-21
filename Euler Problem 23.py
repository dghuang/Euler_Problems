from math import sqrt
t = []
to = 0
a = range(1, 28123)
for x in a:
	c = 1
	d = []
	s = 0
	while c <= sqrt(x):
		if x % c == 0:
			d.append(c)
			if x / c != x:
				d.append(x/c)
		c = c + 1
	for z in d:
		s += z
	if s > x:
		t.append(x)
		if x <= 14061:
			a.remove(x)
r = 0

for x in d:
	if x >r:
		r = x

for x in a:
	if x > r:
		a.remove(x)
		
for x in a:
	for z in t:
		if x - z in a:
			break
	else:
		to += x
	print to
