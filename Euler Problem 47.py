from math import sqrt
a = []
b = [2, 3]
for x in range(1, 2000):
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

a = range(700, 200000)

def checkprimefactors(x):
	z = 0
	for y in b:
		if x % y == 0:
			z = z + 1
		if z == 4:
			break
	if z == 4:
		return True

for x in a:
	if checkprimefactors(x) == True and checkprimefactors(x+1) == True and checkprimefactors(x+2) == True and checkprimefactors(x+3) == True:
		print x
