from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    documents = deque(list(map(int, input().split())))
    count = 0
    while True:
        important_document = max(documents)
        left = documents.popleft()
        if important_document == left:
            count += 1
            if m == 0:
                print(count)
                break
        else:
            documents.append(left)
            if m == 0:
                m = len(documents)
        m -= 1
