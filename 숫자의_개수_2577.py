import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())
abc = str(A * B * C)
for number in "0123456789":
    print(abc.count(number))