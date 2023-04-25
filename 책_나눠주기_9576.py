import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    books = [False] * (n + 1)
    requests = [list(map(int, input().split())) for _ in range(m)]
    requests.sort(key = lambda x:x[1])
    count = 0
    for a, b in requests:
        for i in range(a, b + 1):
            if books[i] == False:
                books[i] = True
                count += 1
                break
    print(count)
