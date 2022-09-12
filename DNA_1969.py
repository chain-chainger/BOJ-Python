n, m = map(int, input().split())
arr = []
res = ""
cnt = 0
for i in range(n):
    arr.append(input())
for i in range(m):
    a = [0 for i in range(26)]
    for j in range(n):
        a[ord(arr[j][i]) - 65] += 1
    res += chr(a.index(max(a)) + 65)
for i in range(n):
    for j in range(m):
        if arr[i][j] != res[j]:
            cnt += 1
print(f"{res}\n{cnt}")