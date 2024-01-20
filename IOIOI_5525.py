n = int(input())
m = int(input())
s = input()
p = "IOI"
answer = 0
count = 0
i = 0

while i < m - 2:
    print(count, i)
    if s[i:i + 3] == p:
        count += 1
        if count >= n:
            print(f"n: {n}, count: {count} s: {s[:i + 3]}")
            answer += 1
        i += 2
    else:
        count = 0
        i += 1
        
print(answer)
