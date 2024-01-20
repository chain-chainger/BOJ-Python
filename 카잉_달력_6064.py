import sys
input = sys.stdin.readline

def solve(m, n, x, y):
    answer = m
    
    while answer < m * n:
        if (answer - x) % m == 0 and (answer - y) % n == 0:
            return answer
        answer += m
    
    return -1

t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    print(solve(m, n, x, y))