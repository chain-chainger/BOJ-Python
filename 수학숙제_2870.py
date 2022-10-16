import re
res = []
n = int(input())
for _ in range(n):
    numbers = re.findall("\d+", input())
    res.extend(list(map(int, numbers)))
print('\n'.join(map(str, sorted(res))))