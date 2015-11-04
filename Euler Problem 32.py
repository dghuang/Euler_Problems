#Problem 32: Find the sum of all products where the multipliers and the product together can be written as a pandigital
#product, ie. the numbers 1-9 are all used exactly once_registry

#the product has to be a 4 digit number, with 2 by 3 multiplication

#create a list of all possible pandigital products

def isPandigital(product):
    for a in range(0,5):
        for b in range(0,4):
            for c in range(0,3):
                for d in range(0,2):
                    nums = range(1,10)
                    for digit in str(product):
                        nums.remove(int(digit))
                    num1 = nums[a]
                    del nums[a]
                    num2 = nums[b]
                    del nums[b]
                    num3 = nums[c]
                    del nums[c]
                    num4 = nums[d]
                    del nums[d]
                    num5 = nums[0]
                    if int(str(num1)+str(num2)) * int(str(num3)+str(num4)+str(num5)) == product or num1 * int(str(num2)+str(num3)+str(num4)+str(num5)) == product:
                        return True
    return False
                    

products = []
pandigital = []
for a in range(0,9):
    for b in range(0,8):
        for c in range(0,7):
            for d in range(0,6):
                nums = range(1,10)
                num1 = nums[a]
                del nums[a]
                num2 = nums[b]
                del nums[b]
                num3 = nums[c]
                del nums[c]
                num4 = nums[d]
                del nums[d]
                products.append(int(str(num1)+str(num2)+str(num3)+str(num4)))
 
for x in products:
    if isPandigital(x) and x not in pandigital:
        pandigital.append(x)

print sum(pandigital)
        