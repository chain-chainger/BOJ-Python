while True:
    s = input()
    if s == "end":
        break
    cnt_v = 0
    same_v, same_c = 0, 0
    flag = True
    for i in range(len(s)):
        if s[i] in "aeiou":
            same_c = 0
            cnt_v += 1
            same_v += 1
            if same_v > 2:
                flag = False
                break
        else:
            same_v = 0
            same_c += 1
            if same_c > 2:
                flag = False
                break
        if i != 0 and s[i] == s[i-1]:
            if s[i] in "eo":
                pass
            else:
                flag = False
                break
    if cnt_v == 0:
        flag = False
    if flag:
        print(f"<{s}> is acceptable.")
    else:
        print(f"<{s}> is not acceptable.")