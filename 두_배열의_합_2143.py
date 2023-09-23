import bisect
import sys
input = sys.stdin.readline

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a_sum = []
b_sum = []
for i in range(n):
    s = a[i]
    a_sum.append(s)
    for j in range(i + 1, n):
        s += a[j]
        a_sum.append(s)
for i in range(m):
    s = b[i]
    b_sum.append(s)
    for j in range(i + 1, m):
        s += b[j]
        b_sum.append(s)
a_sum.sort()
b_sum.sort()
answer = 0
for i in range(len(a_sum)):
    l = bisect.bisect_left(b_sum, t - a_sum[i])
    r = bisect.bisect_right(b_sum, t - a_sum[i])
    answer += r - l
print(answer)