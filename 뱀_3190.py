from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
board = [[0] * (n + 1) for _ in range(n + 1)]
k = int(input())
for _ in range(k):
    row, column = map(int, input().split())
    board[row][column] = 1
turn_information = dict()
l = int(input())
for _ in range(l):
    time_to_play, turn_direction = input().split()
    turn_information[int(time_to_play)] = turn_direction
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
time_to_play = 0
direction = 0
x, y = 1, 1
snake = deque()
snake.append((x, y))
while True:
    time_to_play += 1
    x += dx[direction]
    y += dy[direction]
    if x == 0 or x == (n + 1) or y == 0 or y == (n + 1) or (x, y) in snake:
        break
    snake.append((x, y))
    if board[x][y] == 1:
        board[x][y] = 0
    else:
        tail_x, tail_y = snake.popleft()
    if time_to_play in turn_information:
        if turn_information[time_to_play] == "D":
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4
print(time_to_play)
