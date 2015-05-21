t = 1
r = 0
for n in range(1, 100):
	t = t * n
for x in str(t):
	r = r + int(x)
print r
