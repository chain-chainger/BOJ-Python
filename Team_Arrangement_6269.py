import sys
input = sys.stdin.readline

#input players, formation
players = []
for _ in range(22):
    players.append(input().rstrip().split())
formation = list(map(int, input().rstrip().split('-')))
while True:
    if input().rstrip() == '0':
        break
if sum(formation) != 10 or len(formation) != 3:
    print("IMPOSSIBLE TO ARRANGE")
    exit()
# arrange teama and sort
players.sort(key=lambda x: int(x[0]))
count_g, count_d, count_m, count_s = 0, 0, 0, 0
team = []
for i in range(22):
    if players[i][2] == 'G' and count_g < 1:
        team.append(players[i])
        count_g += 1
    elif players[i][2] == 'D' and count_d < formation[0]:
        team.append(players[i])
        count_d += 1
    elif players[i][2] == 'M' and count_m < formation[1]:
        team.append(players[i])
        count_m += 1
    elif players[i][2] == 'S' and count_s < formation[2]:
        team.append(players[i])
        count_s += 1
if count_g != 1 or count_d != formation[0] or count_m != formation[1] or count_s != formation[2]:
    print("IMPOSSIBLE TO ARRANGE")
    exit()
team.sort(key=lambda x: (x[2], int(x[0])))
# find goalkeeper and captain
for i in range(11):
    if team[i][2] == 'G':
        temp = team.pop(i)
        team.insert(0, temp)
        break
captain_index = 0
longest_record = 0
for i in range(11):
    record = 0
    for j in range(3, len(team[i])):
        start, end = map(int, team[i][j].split('-'))
        record += end - start + 1
    if record >= longest_record:
        if record == longest_record and int(team[i][0]) < int(team[captain_index][0]):
            pass
        else:
            longest_record = record
            captain_index = i
temp = team.pop(captain_index)
team.insert(0, temp)
# print team
for player in team:
    print(*player[:3])