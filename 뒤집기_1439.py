s = input()
cnt_0, cnt_1 = 0, 0
i = 0
while i < len(s):
    if s[i] == '0':
        cnt_0 += 1
        while i < len(s) and s[i] == '0':
            i += 1
    elif s[i] == '1':
        cnt_1 += 1
        while i < len(s) and s[i] == '1':
            i += 1
print(min(cnt_0, cnt_1))