m = int(input())
n = int(input())
arr = []
for i in range(m, n+1):
    if i == 2:
        arr.append(i)
    if i > 2:
        for j in range(2, i):
            if i % j == 0:
                break
            if j == i - 1:
                arr.append(i)
if len(arr) == 0:
    print(-1)
else:
    print(f"{sum(arr)}\n{min(arr)}")