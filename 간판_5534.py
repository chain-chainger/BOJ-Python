n = int(input())
s = input()
cnt = 0
for _ in range(n):
    flag = False
    first_c = 0
    temp = input()
    check = []
    for i in range (len(temp)):
        if temp[i] == s[0] and not flag:
             first_c = i
             flag = True
        if temp[i] == s[1] and flag:
            interval = i - first_c
            check.append(temp[first_c])
            for j in range(i, len(temp), interval):
                check.append(temp[j])
                if len(check) == len(s):
                    break
            if s == ''.join(check):
                cnt += 1
            else:
                check.clear()
print(cnt)