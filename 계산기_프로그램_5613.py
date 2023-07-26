import sys
input = sys.stdin.readline

answer = int(input())
while True:
    operator = input().rstrip()
    if operator == '=':
        break
    n = int(input())
    if operator == '+':
        answer += n
    elif operator == '-':
        answer -= n
    elif operator == '*':
        answer *= n
    elif operator == '/':
        answer //= n
print(answer)