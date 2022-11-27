n = int(input())
a = set(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))
for i in range(m):
    if x[i] in a:
        print(1)
    else:
        print(0)   
