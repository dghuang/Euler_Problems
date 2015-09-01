#Problem 27: Considering the form x^2 + a*x + b, and given that |a| and |b| < 1000, find the product of the values of a and b that
#produce the greatest number of consecutive primes, starting from x = 0

#since starting from x = 0, then b must be a prime Number under 1000
#first produce a list of primes under 1000
b_list = [2]
current_number = 3
while current_number < 1000:
    for x in b_list:
        if current_number % x == 0:
            break
    else:
        b_list.append(current_number)
    current_number = current_number + 2

primes = [2]
current_number = 3
while current_number < 100000:
    for x in primes:
        if current_number % x == 0:
            break
    else:
        primes.append(current_number)
    current_number = current_number + 2
    
maxLength = 0
a = 0
b = 0
for x in b_list:
    for y in range(-999, 1000, 2):
        count = 0
        while (count ** 2 + count * y + x) in primes:
            count = count + 1
        if count > maxLength:
            a = y
            b = x
            maxLength = count
            
print a * b