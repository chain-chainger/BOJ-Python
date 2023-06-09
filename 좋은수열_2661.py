import sys
input = sys.stdin.readline

def recursive(index):
    for i in range(1, (index // 2) + 1):
        if sequence[-i:] == sequence[-2 * i:-i]:
            return -1
    if index == n:
        for i in range(n):
            print(sequence[i], end='')
        return 0
    for i in range(1, 4):
        sequence.append(i)
        if recursive(index + 1) == 0:
            return 0
        sequence.pop()
n = int(input())
sequence = []
recursive(0)