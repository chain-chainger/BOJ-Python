t = int(input())
for _ in range(t):
    arr = [0] * 26
    res = "OK"
    s = input()
    flag = False
    for i in range(len(s)):
        if flag:
            flag = False
            continue
        arr[ord(s[i]) - 65] += 1
        if arr[ord(s[i]) - 65] == 3:
            if i == len(s) - 1 or s[i] != s[i + 1]:
                res = "FAKE"
                break
            flag = True
            arr[ord(s[i]) - 65] = 0
    print(res)