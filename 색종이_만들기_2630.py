import sys
input = sys.stdin.readline

def solve(n, r, c, answer):
    color = paper[r][c]
    for i in range(r, n + r):
        for j in range(c, n+ c):
            if paper[i][j] != color:
                solve(n // 2, r, c, answer)
                solve(n // 2, r, c + n // 2, answer)
                solve(n // 2, r + n // 2, c, answer)
                solve(n // 2, r + n // 2, c + n // 2, answer)
                return
    if color == 0:
        answer.append(0)
    else:
        answer.append(1)

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
answer = []
solve(N, 0, 0, answer)
print(f"{answer.count(0)}\n{answer.count(1)}")