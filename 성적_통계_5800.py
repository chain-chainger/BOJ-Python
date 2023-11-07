import sys
input = sys.stdin.readline

K = int(input())
for i in range(K):
	score_list = list(map(int, input().split()))
	N = score_list[0]
	del score_list[0]
	score_list.sort(reverse=True)
	max_score, min_score = 0, 100
	largest_gap = 0
	for j in range(N):
		if score_list[j] > max_score:
			max_score = score_list[j]
		if score_list[j] < min_score:
			min_score = score_list[j]
		if j < N - 1 and abs(score_list[j] - score_list[j + 1]) > largest_gap:
			largest_gap = abs(score_list[j] - score_list[j + 1])
	print(f"Class {i + 1}")
	print(f"Max {max_score}, Min {min_score}, Largest gap {largest_gap}")
