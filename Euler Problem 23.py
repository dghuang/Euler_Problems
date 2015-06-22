#If an abundant number is defined as a number where the sum of unique divisors is greater than the number
#then find the sum of all numbers under 28123 that cann't be written as a sum of abundant numbers
 
#this function returns true if number is abundant, false if otherwise
def is_abundant(number):
    sum = 1
    for x in xrange(2, int(number**0.5)+1):
        if number % x == 0:
            sum += x + number/x
            if number / x == x: sum -= x
    if sum > number:
        return True
    else:
        return False

#creates a list of all abundant numbers
abundant_list = []
for x in xrange(1, 28124):
    if is_abundant(x):
        abundant_list.append(x)

sums = [False for x in range(1,28124)]

#creates a boolean sums list
for x in abundant_list:
    for y in abundant_list:
        if x + y > 28123:
            break
        else:
            sums[x+y-1] = True
    
number_sum = 0
for x in xrange(0,28123):
    if sums[x] == False:
        number_sum += 1 + x
 
print number_sum