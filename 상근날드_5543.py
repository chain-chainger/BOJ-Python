import sys
input = sys.stdin.readline

bugers = [int(input()) for _ in range(3)]
drinks = [int(input()) for _ in range(2)]
print(min(bugers) + min(drinks) - 50)