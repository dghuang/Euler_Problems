#find the 10000th prime number

prime_list = [2]
number_of_primes = 0
current_number = 3

while number_of_primes <= 10000:
	y = 0
	for x in prime_list:
		if current_number % x == 0:
			break
	else:
		prime_list.append(current_number)
		number_of_primes += 1
	current_number += 2

print prime_list[10000]