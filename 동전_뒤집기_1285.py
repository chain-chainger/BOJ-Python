import sys
input = sys.stdin.readline

N = int(input())
times = list(map(int, input().split()))
answer = 0
times.sort()

for i in range(N):
    answer += sum(times[:i + 1])
    
print(answer)