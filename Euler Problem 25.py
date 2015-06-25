#find the index of the first fibonacci number with 1000 digits

term1 = 1
resultant = 1
index = 2

while len(str(resultant)) != 1000:
    index += 1
    temp = resultant
    resultant += term1
    term1 = temp

print index