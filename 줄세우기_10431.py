import sys
from collections import deque
input = sys.stdin.readline

P = int(input())
for _ in range(P):
    students = list(map(int, input().split()))
    answer = 0
    for i in range(1, 20):
        for j in range(i + 1, 21):
            if students[i] > students[j]:
                students[i], students[j] = students[j], students[i]
                answer += 1
            
    print(students[0], answer)