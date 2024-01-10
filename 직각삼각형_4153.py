import sys
import math
input = sys.stdin.readline

while True:
	triangle_info = list(map(int, input().split()))
	if sum(triangle_info) == 0:
		break
	triangle_info.sort()
	if math.sqrt(math.pow(triangle_info[0], 2) + math.pow(triangle_info[1], 2)) == triangle_info[2]:
		print("right")
	else:
		print("wrong")
