n = int(input())
words = [[0 for _ in range(26)] for _ in range(n)]
res = 0
for i in range(n):
    s = input()
    for c in s:
        words[i][ord(c) - 65] += 1
for word in words[1:]:
    cnt_a, cnt_b = 0, 0
    for i in range(26):
        if word[i] > words[0][i]:
            cnt_a += word[i] - words[0][i]
        else:
            cnt_b += words[0][i] - word[i]
    if cnt_a < 2 and cnt_b < 2:
        res += 1
print(res)