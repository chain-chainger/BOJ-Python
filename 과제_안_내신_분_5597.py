import sys
input = sys.stdin.readline

students = [_ for _ in range(1, 31)]
for _ in range(28):
    temp = int(input())
    students.remove(temp)
print(min(students))
print(max(students))