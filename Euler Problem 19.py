#this is a calendar counting program, the specifics are on Project Euler

year = 1901
b = 29
Sundays = 0

while year != 2001:
	month_list = {1 : range(1,32),
	2 : range(1, 29),
	3 : range(1, 32),
	4 : range(1, 31),
	5 : range(1, 32),
	6 : range(1, 31),
	7 : range(1, 32),
	8 : range(1, 32),
	9 : range(1, 31),
	10 : range(1, 32),
	11 : range(1, 31),
	12 : range(1, 32),}
	if year % 4 == 0:
		month_list[2] = range(1, 30)
		for month in month_list:
			a = len(month_list[month]) % 7
			b = b + a
			if b % 7 == 6:
				Sundays = Sundays + 1
		year = year + 1
	else:
		for month in month_list:
			a = len(month_list[month]) % 7
			b = b + a
			if b % 7 == 6:
				Sundays = Sundays + 1
		year = year + 1

print Sundays
