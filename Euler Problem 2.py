#fibonacci problem: find sum of even fibonacci terms under 4 million

term1, term2, term3, even_sum = 1, 2, 0, 0

while term1 < 4000000:
	term3 = term1 + term2
	term1 = term2
	term2 = term3
	if term1 % 2 == 0:
		even_sum= term1 + even_sum

print even_sum