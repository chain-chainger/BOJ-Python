import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
height = 0
start = 0
end = max(trees)
while start <= end:
    check = 0
    mid = (start + end) // 2
    for tree in trees:
        if tree > mid:
            check += tree - mid
    if check >= m:
        start = mid + 1
        height = max(mid, height)
    else:
        end = mid - 1
print(height)