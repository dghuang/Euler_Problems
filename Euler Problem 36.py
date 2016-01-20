#find sum of all numbers under a million that are palindromes in both base 10 and 2

def isPalindrome(n):
    li = list(str(n))
    l = len(li)
    if l == 1:
        return True
    else:
        for x in range(0, l/2):
            if li[x] != li[l-x-1]:
                return False
        else:
            return True

sum = 0
for x in xrange(1, 1000000):
    #convert the number to binary
    b = int(bin(x)[2:])
    if isPalindrome(x) & isPalindrome(b):
        sum += x

print sum