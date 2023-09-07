import sys
input = sys.stdin.readline

numbers = list(map(int, input().split()))
for i in range(1, len(numbers)):
    if numbers[i] < numbers[i - 1]:
        print("Bad")
        exit()
print("Good")