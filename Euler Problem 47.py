#find the first four consecutive integers to have four distinct prime factors

from math import sqrt
prime_list = [2, 3]

for x in range(5,2001,2):
    c = 0
    while prime_list[c] <= sqrt(x):
        if x % prime_list[c] == 0:
            break
        else: c = c + 1
    else:
        prime_list.append(x)

def checkprimefactors(isprime):
    index = 0
    for prime in prime_list:
        if isprime % prime == 0:
            index += 1
        if index == 4:
            break
    if index == 4:
        return True

while True:
    
    if checkprimefactors(x) == True and checkprimefactors(x+1) == True and checkprimefactors(x+2) == True and checkprimefactors(x+3) == True:
        print x
        break