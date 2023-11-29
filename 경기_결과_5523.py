import sys
input = sys.stdin.readline

N = int(input())
a_count, b_count = 0, 0
for _ in range(N):
	a, b = map(int, input().split())
	if a > b:
		a_count += 1
	elif b > a:
		b_count += 1
print(f"{a_count} {b_count}")
