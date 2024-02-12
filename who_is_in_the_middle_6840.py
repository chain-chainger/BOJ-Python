import sys
input = sys.stdin.readline

numbers = []
for _ in range(3):
    numbers.append(int(input()))
    
print(sorted(numbers)[1])