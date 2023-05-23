import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
if sum(numbers) % 3 == 0:
    print("yes")
else:
    print("no")