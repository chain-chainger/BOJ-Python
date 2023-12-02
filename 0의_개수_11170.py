import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    zero_count = 0
    for i in range (N, M + 1):
        number = str(i)
        for j in range(len(number)):
            if number[j] == '0':
                zero_count += 1
    print(zero_count)