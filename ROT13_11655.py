import sys
input = sys.stdin.readline

s = input().rstrip()
for c in s:
	if 'a' <= c <= 'z':
		print(chr((ord(c) - ord('a') + 13) % 26 + ord('a')), end='')
	elif 'A' <= c <= 'Z':
		print(chr((ord(c) - ord('A') + 13) % 26 + ord('A')), end='')
	else:
		print(c, end='')
