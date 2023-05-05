import sys
input = sys.stdin.readline

n = list(input().rstrip())
sum = 0
for i in range(len(n)):
    sum += int(n[i]) ** 5
print(sum)
