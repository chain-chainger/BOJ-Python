import sys
input = sys.stdin.readline

bugers = [int(input()) for _ in range(3)]
drinks = [int(input()) for _ in range(2)]
# for i in range(5):
#     if i < 3:
#         bugers.append(int(input()))
#     else:
#         drinks.append(int(input()))
print(min(bugers) + min(drinks) - 50)