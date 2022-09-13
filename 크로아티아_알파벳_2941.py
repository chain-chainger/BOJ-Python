croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
s = input()
for target in croatia:
    s = s.replace(target, '1')
print(len(s))