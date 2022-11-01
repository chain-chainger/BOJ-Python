s = input()
res = set()
for i in range(len(s)):
    for j in range(len(s)):
        temp = s[i:j+1]
        res.add(temp)
print(len(res) - 1)