#fibonacci problem: find the sum of all multiples of 3 and 5 under 1000

sum = 0
for x in range(1,1000):
    if (x % 5 == 0) or (x % 3 == 0):
        sum += x

print sum