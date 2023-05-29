import sys
input = sys.stdin.readline

n = int(input())
time = []
for _ in range(n):
	start, end = map(int, input().split())
	time.append([start, end])
time = sorted(time, key=lambda a:a[0])
time = sorted(time, key=lambda a:a[1])
count = 0
last = 0
for start, end in time:
    if start >= last:
        count += 1
        last = end
print(count)
