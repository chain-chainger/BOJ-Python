import sys
input = sys.stdin.readline

p = [0, 1, 1, 1]
for i in range(1, 98):
    p.append(p[i] + p[i+1])    
t = int(input())
for _ in range(t):
    print(p[int(input())])
