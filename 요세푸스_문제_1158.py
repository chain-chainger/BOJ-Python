import sys
input = sys.stdin.readline

n, k = map(int, input().split())
people = [i for i in range(1, n + 1)]
answer = []
while people:
    for _ in range(k - 1):
        people.append(people.pop(0))
    answer.append(people.pop(0))
print("<", end = "")
for i in range(len(answer) - 1):
    print(answer[i], end = ", ")
print(str(answer[len(answer) - 1]) + ">")