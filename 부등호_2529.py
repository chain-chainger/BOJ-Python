import sys
input = sys.stdin.readline

def check(prev, next, sign):
    if sign == '<':
        return prev < next
    else:
        return next < prev

def solve(depth, answer):
    global max_answer, min_answer
    
    if depth == n + 1:
        if not min_answer:
            min_answer = answer
        else:
            max_answer = answer
        return
    for i in range(10):
        if not visited[i]:
            if depth == 0 or check(answer[-1], str(i), signs[depth - 1]):
                visited[i] = 1
                solve(depth + 1, answer + str(i))
                visited[i] = 0

n = int(input())
signs = list(input().split())
visited = [0] * 10
max_answer, min_answer = "", ""
solve(0, "")
print(max_answer + "\n" + min_answer)
