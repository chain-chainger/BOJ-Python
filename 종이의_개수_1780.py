import sys
input = sys.stdin.readline

def dfs(row, col, n):
    global minus_one_count, zero_count, one_count
    current_value = board[row][col]
    for i in range(row, row + n):
        for j in range(col, col + n):
            if board[i][j] != current_value:
                for k in range(3):
                    for l in range(3):
                        dfs(row + k * n // 3, col + l * n // 3, n // 3)
                return
    if current_value == -1:
        minus_one_count += 1
    elif current_value == 0:
        zero_count += 1
    else:
        one_count += 1

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
minus_one_count, zero_count, one_count = 0, 0, 0 
dfs(0, 0, N)
print(f"{minus_one_count}\n{zero_count}\n{one_count}")