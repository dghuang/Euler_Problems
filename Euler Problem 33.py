#Problem 33: Some fractions, if you simply take out the same digit in the numerator and denominator, will give you an equivalent Fraction
#when simplified. Find the denominator of the product of all such fractions, ie. 49/98
#Multiples of 10, ie. 30/50, are considered trivial fractions

#create a list of prime numbers to check against for simplification
primes = [2,3]
for odd in range(5, 99, 2):
    for x in primes:
        if odd % x == 0:
            break
    else:
        primes.append(odd)

#this will simplify any numerator and denominator
def simplify(num, denom):
    i = 0
    while num >= primes[i] and i < len(primes)-1:
        while num / primes[i] >= 1 and num % primes[i] == 0 and denom % primes[i] == 0:
            num = num / primes[i]
            denom = denom / primes[i]
        i += 1
    return [num,denom]

#this creates a dictionary of two digits numbers grouped based on number to be removed
fractions= []
dict = {}
for i in range(1,10):
    dict[i] = []
    for j in range(1,10):
        if j != i:
            dict[i].append(i*10+j)
            dict[i].append(j*10+i)
            
#this checks every list based on the number it is grouped by to see if the 
for i in range(1,10):
    dict[i].sort()
    print dict[i]
    for x in dict[i]:
        for y in dict[i]:
            if x < y:
                if x / 10 == i:
                    newnum = x % 10
                else:
                    newnum = x / 10
                if y / 10 == i:
                    newdenom = y % 10
                else:
                    newdenom = y / 10
                if simplify(x,y)[0] == simplify(newnum, newdenom)[0] and simplify(x,y)[1] == simplify(newnum, newdenom)[1]:
                    fractions.append([x,y])

num = 1
denom = 1
for x in fractions:
    num *= x[0]
    denom *= x[1]

print simplify(num, denom)[1]