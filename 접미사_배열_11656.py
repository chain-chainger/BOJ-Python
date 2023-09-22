import sys
input = sys.stdin.readline

s = input().rstrip()
s_list = []
for i in range(len(s)):
    s_list.append(s[i:])
s_list.sort()
for element in s_list:
    print(element)