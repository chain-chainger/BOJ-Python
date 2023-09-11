import sys
input = sys.stdin.readline

d = list(map(int, input().split()))
a = (d[0] + d[1] - d[2]) / 2
b = d[0] - a
c = d[1] - a
if a > 0 and b > 0 and c > 0:
    print(1)
    print("%.1f %.1f %.1f" % (a, b, c))
else:
    print(-1)