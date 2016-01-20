#a triangle number is one in the sequence 0.5*n*(n+1)
#if the sum of a number is the alphabetical sum of their positions
#find how many sums in the text file are triangle numbers

triNums = []
for x in range(1, 20):
    triNums.append(x * (x+1) / 2)

with open("words_42.txt", "r") as myFile:
    words = myFile.read()

words = words.replace('"', '').split(',')

n = 0
for word in words:
    sum = 0
    for char in word:
        #use ascii values to find character's position
        sum += ord(char) - 64
    if sum in triNums:
        n += 1
        
print n