n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
for i in range(1, n):
    arr[i+1] += arr[i]
for _ in range(m):
    i, j = map(int, input().split())
    print(arr[j] - arr[i-1])