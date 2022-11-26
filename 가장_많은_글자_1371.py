import sys
s = sys.stdin.read()
alphabet = [0] * 26
for c in s:
    if c.islower():
        alphabet[ord(c)-97] += 1
for i in range(len(alphabet)):
    if alphabet[i] == max(alphabet):
        print(chr(i + 97), end='')