import sys
input = sys.stdin.readline

r, c, zr, zc = map(int, input().split())
article = [input().rstrip() for _ in range(r)]
for i in range(r * zr):
    for j in range(c * zc):
        print(article[i // zr][j // zc], end='')
    print()