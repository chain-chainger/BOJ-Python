import sys
input = sys.stdin.readline

N, M = map(int, input().split())
answer = str(N)
for _ in range(1, N):
	answer += str(N)
	if len(answer) >= M:
		break
print(answer[:M])
