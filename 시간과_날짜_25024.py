import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    if x <= 23 and y <= 59:
        print("Yes", end=" ")
    else:
        print("No", end=" ")
    if x <= 12:
        if x == 2 and y <= 29 and y > 0:
            print("Yes")
        elif x in {1, 3, 5, 7, 8, 10, 12} and y <= 31 and y > 0:
            print("Yes")
        elif x in {4, 6, 9, 11} and y <= 30 and y > 0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
