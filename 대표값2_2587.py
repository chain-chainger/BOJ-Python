import sys
input = sys.stdin.readline

sequence = []
for _ in range(5):
	sequence.append(int(input()))
sequence.sort()
print(int(sum(sequence) / 5))
print(sequence[2])
