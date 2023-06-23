import sys
input = sys.stdin.readline

m, n = map(int, input().split())
lengths = list(map(int, input().split()))
start = 1
end = max(lengths)
answer = 0
while start <= end:
    count = 0
    mid = (start + end) // 2
    if mid == 0:
        break
    for length in lengths:
        if length >= mid:
            count += (length // mid)
    if count >= m:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
print(answer)