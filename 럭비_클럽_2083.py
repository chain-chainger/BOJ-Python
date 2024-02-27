import sys
input = sys.stdin.readline

while True:
	name, age, weight = input().rstrip().split()

	if name == '#' and age == '0' and weight == '0':
		break

	if int(age) > 17 or int(weight) >= 80:
		print(f"{name} Senior")
	else:
		print(f"{name} Junior")
