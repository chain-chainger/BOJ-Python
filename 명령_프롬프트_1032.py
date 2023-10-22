import sys
input = sys.stdin.readline

N = int(input())
file_names = []
for _ in range(N):
	file_names.append(input().rstrip())
answer = list(file_names[0])
for i in range(1, N):
	for j in range(len(answer)):
		if answer[j] != '?' and answer[j] != file_names[i][j]:
			answer[j] = '?'
print(''.join(answer))
