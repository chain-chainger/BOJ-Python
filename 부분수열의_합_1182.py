import sys
input = sys.stdin.readline

def solve(start):
    global count
    if sum(temp) == s and len(temp):
        count += 1
    for i in range(start, n):
        temp.append(sequence[i])
        solve(i + 1)
        temp.pop()

n, s = map(int, input().split())
sequence = list(map(int, input().split()))
count = 0
temp = []
solve(0)
print(count)