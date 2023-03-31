import sys
input = sys.stdin.readline

apple, banana = 0, 0
for i in range(3):
    apple += int(input()) * (3 - i)
for i in range(3):
    banana += int(input()) * (3 - i)
if apple > banana:
    print("A")
elif apple < banana:
    print("B")
else:
    print("T")