import sys
input = sys.stdin.readline

digits = input().rstrip()
if digits[:3] == "555":
    print("YES")
else:
    print("NO")