import sys
import math
input = sys.stdin.readline

L = int(input())
target = input().rstrip()
answer = 0

for i in range(L):
    number = ord(target[i]) - 96
    number *= pow(31, i)
    answer += number
    
print(answer % 1234567891)