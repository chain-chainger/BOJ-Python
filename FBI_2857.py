res = []
for i in range(5):
    s = input()
    if "FBI" in s:
        res.append(i + 1)
if res:
    print(*res)
else:
    print("HE GOT AWAY!")