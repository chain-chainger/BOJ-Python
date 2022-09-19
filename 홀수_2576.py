odd_n = []
for _ in range(7):
    n = int(input())
    if n % 2 == 1:
        odd_n.append(n)
if odd_n:
    print(f"{sum(odd_n)}\n{min(odd_n)}")
else:
    print(-1)