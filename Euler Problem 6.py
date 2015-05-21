#find difference between sum of numbers from 1-100 and sum of their squares

sum_squares = 0
squared_sum = (100*51)**2 #by gaussian sum

for x in range (1, 101):
	sum_squares += x**2

print squared_sum - sum_squares