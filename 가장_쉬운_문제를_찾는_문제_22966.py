import sys
input = sys.stdin.readline

n = int(input())
problems = [list(input().rstrip().split()) for _ in range(n)]
problems.sort(key = lambda x:x[1])
print(problems[0][0])
