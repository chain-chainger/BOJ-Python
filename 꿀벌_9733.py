import sys
dic = {"Re":0, "Pt":0, "Cc":0, "Ea":0, "Tb":0, "Cm":0, "Ex":0}
action = []
cnt = 0
lines = sys.stdin.readlines()
for line in lines:
    action = line.split()
    cnt += len(action)
    for s in action:
        if s in dic.keys():
            dic[s] += 1
for s in dic.keys():
    print(f"{s} {dic.get(s)} {dic.get(s) / cnt:.2f}")
print(f"Total {cnt} 1.00")
