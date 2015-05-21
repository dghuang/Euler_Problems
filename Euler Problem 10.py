#find sum of all primes under 2 million

prime_list = [2]
current_number = 3

while current_number < 2*10**6:
	for x in prime_list:
		if x > current_number**0.5:
			prime_list.append(current_number)
			break
		elif current_number % x == 0:
			break
	current_number += 2

prime_sum = 0
for x in prime_list:
	prime_sum += x
print prime_sum
