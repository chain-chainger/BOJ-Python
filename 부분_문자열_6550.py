while True:
    try:
        s, t = input().split()
        i_s = 0
        flag = 0
        for i in range(len(t)):
            if t[i] == s[i_s]:
                i_s += 1
            if i_s == len(s):
                flag = 1
                break
        if flag:
            print("Yes")
        else:
            print("No")
    except:
        break