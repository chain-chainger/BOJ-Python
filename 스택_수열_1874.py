import sys
input = sys.stdin.readline

n = int(input())
stack = []
answers = []
current = 1
for _ in range(n):
    num = int(input())
    while current <= num:
        stack.append(current)
        answers.append("+")
        current += 1
    if stack[-1] == num:
        stack.pop()
        answers.append("-")
    else:
        print("NO")
        exit()
for answer in answers:
    print(answer)