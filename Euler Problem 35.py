#Find all numbers that can be written as a sum of the factorial of their digits, eg. 145 = 1! + 4! + 5!

def factorial(n):
    if n == 1: return 1
    else: return n * factorial(n-1)

#it's faster to have a quick reference guide than to call the factorial function every time it needs to be calculated
fact = []
for i in range(1, 10):
    fact.append(factorial(i))