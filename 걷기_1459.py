import sys
input = sys.stdin.readline

x, y, w, s = map(int, input().split())
if s > w * 2:
    print((x + y) * w)
else:
    if x > y:
        count_s = y
    else:
        count_s = x
    x -= count_s
    y -= count_s
    if s < w and (x + y) != 0:
        if (x + y) % 2 == 0:
            print((count_s * s) + (x + y) * s)
        else:
            print((count_s * s) + ((x + y - 1) * s + w))
    else:
        print((count_s * s) + ((x + y) * w))
