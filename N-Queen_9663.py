import sys
input = sys.stdin.readline

def check_value(index):
    for i in range(index):
        if board[index] == board[i] or abs(board[index] - board[i]) == abs(index - i):
            return False
    return True

def solve(index):
    global count
    if index == n:
        count += 1
        return
    for i in range(n):
        board[index] = i
        if check_value(index) == True:
            solve(index + 1)

n = int(input())
board = [0] * n
count = 0
solve(0)
print(count)