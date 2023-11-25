import sys
input = sys.stdin.readline

N = int(input())
a, b = list(input().rstrip()), list(input().rstrip())
if N % 2 == 1:
	for i in range(len(a)):
		if a[i] == '0':
			a[i] = '1'
		else:
			a[i] = '0'
if a == b:
	print("Deletion succeeded")
else:
	print("Deletion failed")
