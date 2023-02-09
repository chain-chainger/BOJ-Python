import sys
input = sys.stdin.readline

n = int(input())
months = [0] * 13
for _ in range(n):
    month = input().split()[1].split('/')[1]
    months[int(month)] += 1
for i in range(1, 13):
    print(i, months[i])
