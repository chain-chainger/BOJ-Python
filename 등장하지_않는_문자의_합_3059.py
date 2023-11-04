import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    S = input().rstrip()
    answer = 0
    for c in range(65, 91):
        if chr(c) not in S:
            answer += c
    print(answer)
