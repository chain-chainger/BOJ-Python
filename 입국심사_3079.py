import sys
input = sys.stdin.readline

n, m = map(int, input().split())
t = [int(input()) for _ in range(n)]
start, end, time = min(t), min(t) * m, 0
while start <= end:
    mid = (start + end) // 2
    count = 0
    for time_to_immigration in t:
        count += mid // time_to_immigration
        if count > m:
            break
    if count >= m:
        end = mid - 1
        time = mid
    else:
        start = mid + 1
print(time)