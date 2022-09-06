t = int(input())
for i in range(t):
    n = int(input())
    start = input()
    goal = input()
    diff = []
    for j in range(n):
        if start[j] != goal[j]:
            diff.append(start[j])
    if diff.count('W') >= diff.count('B'):
        print(diff.count('W'))
    else :
        print(diff.count('B'))