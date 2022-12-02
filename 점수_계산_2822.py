scores = []
high_scores = []
sum = 0
for i in range(8):
	scores.append(int(input()))
for i in range(5):
	high_scores.append(scores.index(max(scores)) + 1)
	sum += scores[scores.index(max(scores))]
	scores[scores.index(max(scores))] = 0
high_scores.sort()
print(sum)
print(*high_scores)
