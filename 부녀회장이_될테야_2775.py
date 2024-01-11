import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    floor_info = [i for i in range(1, n + 1)]
    current_floor = 0
    while current_floor < k:
        temp_info = []
        for i in range(n):
            temp_info.append(sum(floor_info[:i + 1]))
        floor_info = temp_info
        current_floor += 1
    print(floor_info[n - 1])
            