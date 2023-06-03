from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
houses = []
restaurants = []
answer = 10 ** 5
for i in range(n):
	for j in range(n):
		if city[i][j] == 1:
			houses.append([i, j])
		elif city[i][j] == 2:
			restaurants.append([i, j])
for restaurant in combinations(restaurants, m):
	sum_distance = 0
	for house in houses:
		distance = 10 ** 5
		for i in range(m):
			distance = min(distance, abs(house[0] - restaurant[i][0]) + abs(house[1] - restaurant[i][1]))
		sum_distance += distance
	answer = min(answer, sum_distance)
print(answer)
