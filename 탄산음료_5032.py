import sys
input = sys.stdin.readline

e, f, c = map(int, input().split())
n = e + f
answer = n // c
while n >= c:
    n = (n // c) + (n % c)
    answer += n // c
print(answer)
