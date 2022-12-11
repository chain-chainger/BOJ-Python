a, b = map(int, input().split())
if a - (b / 100 * a) < 100:
    print(1)
else:
    print(0)