import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
numbers = [i for i in range(1, N + 1)]
numbers = deque(numbers)
numbers_len = N

while numbers_len > 1:
	numbers.popleft()
	numbers_len -= 1
	numbers.rotate(-1)

print(numbers[0])
