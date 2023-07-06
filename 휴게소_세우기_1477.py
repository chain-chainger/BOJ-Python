import sys
input = sys.stdin.readline

n, m, l = map(int, input().split())
arr = [0] + list(map(int, input().split())) + [l]
arr.sort()
start, end = 1, l - 1
answer = 0
while start <= end:
    count = 0
    mid = (start + end) // 2
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] > mid:
            count += (arr[i] - arr[i - 1] - 1) // mid
    if count > m:
        start = mid + 1
    else:
        end = mid - 1
        answer = mid
print(answer)
