import sys
input = sys.stdin.readline

n, k = map(int, input().split())
people = [i for i in range(1, n + 1)]
answer = []
num = 0
for i in range(n):
    num += (k - 1)
    if num >= len(people):
        num %= len(people)
    answer.append(str(people[num]))
    people.pop(num)
print("<", ", ".join(answer), ">", sep="")