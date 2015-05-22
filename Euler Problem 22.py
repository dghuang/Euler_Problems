#an amicable pair is a pair where both the numbers have divisors that add up to each other
#find sum of all amicable pairs under 10000

def divisor_sum(n):
    sum = 0
    for i in range(1, int(n**0.5)):
        if n % i == 0:
            sum += i + n/i
    sum -= n
    return sum

amicable_numbers = {}
amicable_sum = 0
for i in range(220, 10001):
    if not i in amicable_numbers:
        if divisor_sum(divisor_sum(i)) == i and i != divisor_sum(i):
            amicable_numbers[i] = True
            amicable_numbers[divisor_sum(i)] = True
  
for n in amicable_numbers.keys():
    if amicable_numbers[n]:
        amicable_sum += n
        
print amicable_sum   