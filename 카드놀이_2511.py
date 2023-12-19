import sys
input = sys.stdin.readline

a_score = list(map(int, input().split()))
b_score = list(map(int, input().split()))
a_win, b_win = 0, 0
result = []

for i in range(10):
    if a_score[i] > b_score[i]:
        a_win += 3
        result.append("A")
    elif b_score[i] > a_score[i]:
        b_win += 3
        result.append("B")
    else:
        a_win += 1
        b_win += 1
        result.append("D")

print(a_win, b_win)
if a_win == b_win:
    for i in range(9, -1, -1):
        if result[i] != "D" or i == 0:
            print(result[i])
            break
elif a_win > b_win:
    print("A")
else:
    print("B")
    