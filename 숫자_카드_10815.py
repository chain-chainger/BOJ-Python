n = int(input())
list_n = list(map(int, input().split()))
m = int(input())
list_m = list(map(int, input().split()))
for i in range(m):
    if list_m[i] in list_n:
        print(1, end=' ')
    else:
        print(0, end=' ')