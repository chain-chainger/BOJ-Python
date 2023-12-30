import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot_position = deque([0] * N)
answer = 0

while True:
    answer += 1
    belt.rotate(1)
    robot_position.rotate(1)
    robot_position[N - 1] = 0
    for i in range(N - 1, 1, -1):
        if robot_position[i - 1] == 1 and robot_position[i] == 0 and belt[i] > 0:
            robot_position[i] = 1
            robot_position[i - 1] = 0
            belt[i] -= 1
    robot_position[N - 1] = 0
    if belt[0] > 0:
        robot_position[0] = 1
        belt[0] -= 1
    if belt.count(0) >= K:
        break
    
print(answer)