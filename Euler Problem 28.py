#Problem 28: if a 1001 by 1001 number spiral is formed, counting from 1 upwards, what is the sum of the diagonals of the formed spiral
#very simple, simple algorithm with addition based on number of sides

sum = 1
num = 1
side = 3

while side <= 1001:
    sum = sum + 4 * num + 10 * (side - 1)
    num = num + 4 * (side - 1)
    side = side + 2

print sum