import sys
input = sys.stdin.readline

while True:
	info = list(map(int, input().split()))
	
	if len(info) == 1 and info[0] == 0:
		break
	
	answer = 1
	for i in range(1, len(info), 2):
		answer *= info[i]
		answer -= info[i + 1]

	print(answer) 
