import sys
input = sys.stdin.readline

proper_pieces = [1, 1, 2, 2, 2, 8]
input_pieces = list(map(int, input().split()))
answer = []

for i in range(6):
	answer.append(proper_pieces[i] - input_pieces[i])

print(*answer)
