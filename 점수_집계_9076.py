import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    numbers = list(map(int, input().split()))
    numbers.sort()
    if numbers[3] - numbers[1] >= 4:
        print("KIN")
    else:
        print(sum(numbers[1 : 4]))