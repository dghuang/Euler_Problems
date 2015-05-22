#collatz sequence: given a starting number, if it is even, divide by 2, if odd, 3n + 1
#if all collatz sequences end at 1 find the largest chain of numbers under a million

longest_chain = 0
for number in range (1, 1000000):
	chain_length = 0
	term_value = number
	while term_value != 1:
		if term_value % 2 == 0 and term_value > 1:
			term_value /= 2
			chain_length += 1
		else:
			term_value = 3 * term_value + 1
			chain_length += 1
	if chain_length > longest_chain:
		longest_chain = chain_length

print longest_chain