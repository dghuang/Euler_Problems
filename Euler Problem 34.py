#Find all numbers that can be written as a sum of the factorial of their digits, eg. 145 = 1! + 4! + 5!

def factorial(n):
    if n == 1: return 1
    else: return n * factorial(n-1)
    
def digits(n):
    s = list(str(n))
    digits = map(int, s)
    return digits

def isCurious(n):
    sum = 0
    for digit in digits(n):
        sum += fact[digit]
    return n == sum

#it's faster to have a quick reference guide than to call the factorial function every time it needs to be calculated
fact = [1]
for i in range(1, 10):
    fact.append(factorial(i))

sum = 0
for x in range(3, 2000000):
    if isCurious(x):
        sum += x

print sum