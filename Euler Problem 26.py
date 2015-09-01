#Problem 26: find the number under 1000 that has the longest digit recurring cycle
#for a number n, the recurring part of 1/n will never have more than n-1 digits
#knowing this, the algorithm becomes easy to solve

def findDigits(n):
    digits_list = []
    divisor = 10
    for x in range(1, n*2-1):
        if divisor == 0:
            break
        while divisor < n:
            divisor = divisor * 10
            digits_list.append(0)
        digits_list.append(divisor/n)
        divisor = divisor % n
    return digits_list

def isReccuring(list):
    count = len(list) - 3
    while count >= len(list)/2:
        if list[count] == list[len(list)-1]:
            count2 = 1
            while count2 < len(list)-1 - count:
                if list[count-count2] != list[len(list)-1-count2]:
                    break
                count2 = count2 + 1
            else:
                return count2
        count = count - 1
 
length = 0
maxNum = 0       
for x in range(7,1000, 2):
    tempLength = isReccuring(findDigits(x))
    if tempLength > length:
        length = tempLength
        maxNum = x
           
print maxNum