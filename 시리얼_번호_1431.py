import sys
input = sys.stdin.readline

def serial_number_sum(serial_number):
	sum = 0
	for i in serial_number:
		if i.isdigit():
			sum += int(i)
	return sum

def serial_number_compare(a, b):
	if len(a) != len(b):
		return len(a) < len(b)
	if serial_number_sum(a) != serial_number_sum(b):
		return serial_number_sum(a) < serial_number_sum(b)
	for i in range(len(a)):
		if a[i] != b[i]:
			if a[i].isdigit() and not b[i].isdigit():
				return True
			if not a[i].isdigit() and b[i].isdigit():
				return False
			return a[i] < b[i]

n = int(input())
serial_numbers = []

for _ in range(n):
	serial_number = input().strip()

	if len(serial_numbers) == 0:
		serial_numbers.append(serial_number)
		continue

	for i in range(len(serial_numbers)):
		if serial_number_compare(serial_number, serial_numbers[i]):
			serial_numbers.insert(i, serial_number)
			break
		if i == len(serial_numbers) - 1:
			serial_numbers.append(serial_number)

print("\n".join(serial_numbers))
