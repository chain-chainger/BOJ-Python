t = int(input())
for _ in range(t):
    s = input().split()
    sounds = []
    res = []
    while True:
        temp = input()
        if temp == "what does the fox say?":
            break
        temp = temp.split(" goes ")
        sounds.append(temp[1])
    for word in s:
        if word not in sounds:
            res.append(word)
    print(' '.join(res))