m = int(input())
arr = [0, 1, 2, 3]
for _ in range(m):
    x, y = map(int, input().split())
    if x == y:
        continue
    arr[x], arr[y] = arr[y], arr[x]
print(arr.index(1))