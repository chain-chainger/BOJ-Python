import sys
from collections import deque
input = sys.stdin.readline

def bfs(relationships, start):
    answer = [0] * (n + 1)
    visited = [start]
    queue = deque([start])

    while queue:
        current = queue.popleft()
        for next_user in relationships[current]:
            if next_user not in visited:
                queue.append(next_user)
                visited.append(next_user)
                answer[next_user] = answer[current] + 1

    return sum(answer)

if __name__ == '__main__':
    n, m = map(int, input().split())
    relationships = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        a, b = map(int, input().split())
        relationships[a].append(b)
        relationships[b].append(a)

    answers = []
    for i in range(1, n + 1):
        answers.append(bfs(relationships, i))

    print(answers.index(min(answers)) + 1)