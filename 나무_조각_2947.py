import sys
input = sys.stdin.readline

numbers = list(map(int, input().split()))
while True:
    if numbers == [1, 2, 3, 4 , 5]:
        break
    for i in range(1, 5):
        if numbers[i] < numbers[i - 1]:
            temp = numbers[i]
            numbers[i] = numbers[i - 1]
            numbers[i - 1] = temp
            print(*numbers)
            