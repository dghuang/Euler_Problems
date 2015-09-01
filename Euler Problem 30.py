#Problem 30: Find the sum of all numbers that can be written as the sum of fifth powers of their digits
#1^5 is excluded as it doesn't count as a sum

sum = 0
#only numbers from 2 to 1000000 need to be considered, since with numbers greater than a million, your fifth power digit sum will
#never reach 1 million
for x in range(2, 1000000):
    string = str(x)
    numsum = 0
    for char in string:
        numsum = numsum + int(char)**5
    if numsum == x:
        sum = sum + x
        
print sum