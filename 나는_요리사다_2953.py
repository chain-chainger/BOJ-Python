scores = []
for _ in range(5):
    scores.append(sum(list(map(int, input().split()))))
print(scores.index(max(scores)) + 1, max(scores))