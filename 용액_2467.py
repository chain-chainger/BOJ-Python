import sys
input = sys.stdin.readline

n = int(input())
liquids = list(map(int, input().split()))
answer = 20 ** 9
left = 0
right = 0
for i in range(n):
    current = liquids[i]
    start = i + 1
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        temp = current + liquids[mid]
        if abs(temp) < answer:
            answer = abs(temp)
            left = i
            right = mid
            if temp == 0:
                break
        if temp < 0:
            start = mid + 1
        else:
            end = mid - 1
print(liquids[left], liquids[right])