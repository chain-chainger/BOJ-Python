import sys
input = sys.stdin.readline

n = int(input())
numbers = set(map(int, input().split()))
print(*sorted(list(numbers)))
