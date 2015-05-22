from math import sqrt

prime_list = [2, 3]
for x in range(5, 1000000, 2):
    index = 0
    while prime_list[index] <= sqrt(x):
        if x % prime_list[index] == 0:
            break
        else: index += 1
    else:
        prime_list.append(x)
longest_chain = 0

#this prints the prime and the number in its chain
for x in prime_list:
    chain_length = 0
    longest_prime = 0
    prime_number = prime_list.index(x)
    while longest_prime < 1000000:
        longest_prime += prime_list[prime_number]
        chain_length += 1
        if longest_prime in prime_list and chain_length > longest_chain:
            longest_chain = chain_length
            print longest_prime
            print longest_chain
        prime_number += 1
