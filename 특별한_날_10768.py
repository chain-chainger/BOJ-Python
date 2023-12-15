import sys
input = sys.stdin.readline

month = int(input())
day = int(input())

if month == 1:
	print("Before")
elif month == 2:
	if month == 2 and day < 18:
		print("Before")
	elif month == 2 and day == 18:
		print("Special")
	else:
		print("After")
else:
	print("After")
