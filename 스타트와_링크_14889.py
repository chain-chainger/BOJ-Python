import sys
input = sys.stdin.readline

def cal_diff(team1, team2):
    sum_team1 = 0
    sum_team2 = 0
    for i in range(len(team1)):
        for j in range(len(team2)):
            sum_team1 += s[team1[i]][team1[j]]
            sum_team2 += s[team2[i]][team2[j]]
    return abs(sum_team1 - sum_team2)

def make_team(team1, count, n, start):
    global answer
    if count > 0 and team1[0] != 0:
        return
    if count == n // 2:
        team2 = []
        for index in range(n):
            if index not in team1:
                team2.append(index)
        diff = cal_diff(team1, team2)
        answer = min(answer, diff)
        return
    for index in range(start, n):
        if index not in team1:
            team1.append(index)
            make_team(team1, count + 1, n, index + 1)
            team1.remove(index)

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
answer = int(1e9)
make_team([], 0, n, 0)
print(answer)