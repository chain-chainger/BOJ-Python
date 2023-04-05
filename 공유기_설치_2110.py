import sys
input = sys.stdin.readline

n, c = map(int, input().split())
positions = [int(input()) for _ in range(n)]
positions.sort()
start = 1
end = positions[-1] - positions[0]
answer = 0
while start <= end:
    mid = (start + end) // 2
    current = positions[0]
    count = 1
    for i in range(1, n):
        if positions[i] >= current + mid:
            count += 1
            current = positions[i]
    if count >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
print(answer)