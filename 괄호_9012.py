t = int(input())
for _ in range(t):
    s = input()
    check = 0
    for i in range(len(s)):
        if s[i] == '(':
            check += 1
        elif s[i] == ')':
            check -= 1
        if check < 0:
            print("NO")
            break
    if check == 0:
        print("YES")
    elif check > 0:
        print("NO")