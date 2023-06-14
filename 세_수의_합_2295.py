import sys
input = sys.stdin.readline

n = int(input())
u = [int(input()) for _ in range(n)]
a_plus_b = set()
for i in u:
    for j in u:
        a_plus_b.add(i + j)
k_list = set()
for i in u:
    for j in u:
        if (i - j) in a_plus_b:
            k_list.add(i)
print(max(k_list))