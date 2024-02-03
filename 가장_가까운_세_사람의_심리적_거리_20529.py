import sys
from itertools import combinations
input = sys.stdin.readline

t = int(input())

for _ in range(t):
	n = int(input())
	mbtis = list(input().rstrip().split())
	if n >= 33:
		print(0)
	else:
		answer = 8
		cases = combinations(mbtis, 3)

		for a, b, c in cases:
			mbti_dist = 0
			for i in range(4):
				if a[i] != b[i]:
					mbti_dist += 1
				if a[i] != c[i]:
					mbti_dist += 1
				if b[i] != c[i]:
					mbti_dist += 1
			if answer > mbti_dist:
				answer = mbti_dist

		print(answer)
