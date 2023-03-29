n = int(input())
m = int(input())
s = input()
p = "IO" * n + "I"
i = 0
cnt = 0
while i < m:
    if s[i:i+len(p)] == p:
        cnt += 1
    i += 1
print(cnt)
