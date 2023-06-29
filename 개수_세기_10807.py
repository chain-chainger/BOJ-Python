import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
v = int(input())
print(numbers.count(v))