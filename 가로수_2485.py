from math import gcd
n = int(input())
interval = []
num = int(input())
for _ in range(n - 1):
    temp = int(input())
    interval.append(temp - num)
    num = temp
interval_gcd = interval[0]
for i in range(1, n - 1):
    interval_gcd = gcd(interval_gcd, interval[i])
res = 0
for value in interval:
    res += value // interval_gcd - 1
print(res)