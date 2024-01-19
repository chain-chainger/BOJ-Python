import sys
input = sys.stdin.readline

n = input().rstrip()
m = int(input())
if m == 0:
    broken_numbers = []
else:
    broken_numbers = input().rstrip().split()
answer = abs(100 - int(n))

for channel in range(1000001):
    for number in str(channel):
        if number in broken_numbers:
            break
    else:
        answer = min(answer, len(str(channel)) + abs(channel - int(n)))

print(answer)