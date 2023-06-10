from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = input().rstrip()
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(','))
    if n == 0:
        arr = []
    count_R = 0
    flag = False
    for func in p:
        if func == 'R':
            count_R += 1
        else:
            if len(arr) == 0:
                print("error")
                flag = True
                break
            if count_R % 2 == 1:
                arr.pop()
            else:
                arr.popleft()
    if flag:
        continue
    if count_R % 2 == 1:
        arr.reverse()
    print('[' + ','.join(arr) + ']')
    