import sys
input = sys.stdin.readline

n = int(input())
abc = map(int, input().split())
count = 0
for num in abc:
    if num > n:
        count += n
    else:
        count += num
print(count)

