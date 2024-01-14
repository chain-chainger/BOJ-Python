import sys
input = sys.stdin.readline

def solve(n, r, c):
    if n == 0:
        return 0
    
    n -= 1
    size = 2 ** n
    answer = 0
    
    if r >= size and c >= size:
        answer = size ** 2 * 3
        r -= size
        c -= size
    elif r >= size and c < size:
        answer = size ** 2 * 2
        r -= size
    elif r < size and c >= size:
        answer = size ** 2
        c -= size
        
    return answer + solve(n, r, c)
    
    

N, r, c = map(int, input().split())

print(solve(N, r, c))