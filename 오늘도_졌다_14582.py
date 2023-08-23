import sys
input = sys.stdin.readline

a = list(map(int, input().split()))
b = list(map(int, input().split()))
flag = False
a_sum = b_sum = 0
for i in range(9):
    a_sum += a[i]
    b_sum += b[i]
    if a_sum > b_sum:
        flag = True
print("Yes" if flag else "No")
