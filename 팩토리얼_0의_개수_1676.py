import sys
import math
input = sys.stdin.readline

N = int(input())
N_factorial = math.factorial(N)
answer = 0

for digit in str(N_factorial)[::-1]:
    if digit == '0':
        answer += 1
    else:
        break

print(answer)