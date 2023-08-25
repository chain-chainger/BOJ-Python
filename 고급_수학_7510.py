import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    data = sorted(map(int, input().split()))
    if data[0] ** 2 + data[1] ** 2 == data[2] ** 2:
        print(f"Scenario #{i + 1}:")
        print("yes\n")
    else:
        print(f"Scenario #{i + 1}:")
        print("no\n")