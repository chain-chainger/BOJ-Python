import sys
input = sys.stdin.readline

caesar_code = input().rstrip()
for c in caesar_code:
    if ord(c) < 68:
        print(chr(ord(c) + 23), end='')
    else:
        print(chr(ord(c) - 3), end='')