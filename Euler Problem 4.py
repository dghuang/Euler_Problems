#find largest palindrome made by product of three digit numbers

highest_palindrome = 0
for x in range(100, 1000):
	for y in range(100, 1000):
		product = x*y
		str_product = str(product)
		length = len(str_product)
		if length % 2 == 0:		#converts product into string for easy character comparison
			for char in range(0, length/2):
				if str_product[char] != str_product[length - char - 1]:
					break
			else:
				if product > highest_palindrome:
					highest_palindrome = product
		if length % 2 == 1:
			for char in range(0, length/2 - 1):
				if str_product[char] != str_product[length - char - 1]:
					break
			else:
				if product > highest_palindrome:
					highest_palindrome = product

print highest_palindrome