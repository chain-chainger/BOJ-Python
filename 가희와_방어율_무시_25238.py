a, b = map(int, input().split())
if a * (1 - (b / 100)) < 100:
    print(1)
else:
    print(0)