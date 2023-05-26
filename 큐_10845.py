import sys
input = sys.stdin.readline

n = int(input())
queue = []
for _ in range(n):
    command = input().rstrip().split()
    if command[0] == "push":
        queue.insert(0, command[1])
    elif command[0] == "pop":
        if len(queue):
            print(queue.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        if len(queue):
            print(0)
        else:
            print(1)
    elif command[0] == "front":
        if len(queue):
            print(queue[-1])
        else:
            print(-1)
    elif command[0] == "back":
        if len(queue):
            print(queue[0])
        else:
            print(-1)