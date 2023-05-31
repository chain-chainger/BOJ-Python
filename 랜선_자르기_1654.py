import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]
start = 1
end = max(lan)
while start <= end:
    mid = (start + end) // 2
    count = 0
    for length in lan:
        count += length // mid
    if count >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)
