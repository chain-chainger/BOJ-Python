t = int(input())
for _ in range(t):
    n = int(input())
    total_c = 0
    gpa = 0
    for _ in range(n):
        c, g = map(str, input().split())
        total_c += int(c)
        gpa += float(c) * float(g)
    print(total_c, round(gpa / total_c, 1))