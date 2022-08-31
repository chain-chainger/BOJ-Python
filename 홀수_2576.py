oddN = []
for _ in range(7):
    n = int(input())
    if n % 2 == 1:
        oddN.append(n)
if oddN:
    print(f"{sum(oddN)}\n{min(oddN)}")
else:
    print(-1)