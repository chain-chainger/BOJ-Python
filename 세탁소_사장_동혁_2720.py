import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
	qdnp = [0] * 4
	C = int(input())
	if C // 25 > 0:
		qdnp[0] += C // 25
		C = C % 25
	if C // 10 > 0:
		qdnp[1] += C // 10
		C = C % 10
	if C // 5 > 0:
		qdnp[2] += C // 5
		C = C % 5
	qdnp[3] += C
	print(*qdnp)
