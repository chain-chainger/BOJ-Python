w_scores = [int(input()) for _ in range(10)]
k_scores = [int(input()) for _ in range(10)]
print(sum(sorted(w_scores)[7:]), sum(sorted(k_scores)[7:]))