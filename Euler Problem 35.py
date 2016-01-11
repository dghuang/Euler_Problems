#A circular prime is a number where all rotations of the number are also prime
#Find number of circular primes under a million

#generate all primes up to a certain number
#this saves time so you don't have to check if every number is prime individually
def generatePrimes(n):
    if n <= 1:
        return []
    elif n == 2:
        return [2]
    elif n == 3:
        return [2, 3]
    primes = [2]
    for x in xrange(3, n, 2):
        ind = 0
        limit = n**0.5
        while ind < len(primes) and primes[ind] < limit:
            if x % primes[ind] == 0:
                break
            ind += 1
        else:
            primes.append(x)
    return primes

#generates rotations of a number
def rotations(num):
    l = list(str(num))
    rot = []
    for x in range(0, len(l)):
        rotation = ""
        for y in range(0, len(l)):
            if x+y == 0:
                rotation += l[0]
            else:
                ind = (x + y) % len(l)
                rotation += l[ind]
        rot.append(int(rotation))
    return rot

#saves time by only checking rotations of primes to see if they are all prime
primes = generatePrimes(1000000)
circulars = []
for p in primes:
    if p in circulars:
        continue
    rot = rotations(p)
    for r in rot:
        if r not in primes:
            break
    else:
        for temp in rot:
            if temp not in circulars:
                circulars.append(temp)

print len(circulars)