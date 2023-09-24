import bisect
import sys
input = sys.stdin.readline

N = int(input())
A, B, C, D = [], [], [], []
for _ in range(N):
	a, b, c, d = map(int,input().split())
	A.append(a)
	B.append(b)
	C.append(c)
	D.append(d)
ab, cd = [], []
for i in range(N):
	for j in range(N):
		ab.append(A[i] + B[j])
		cd.append(C[i] + D[j])
ab.sort()
cd.sort()
left, right = 0, len(cd) - 1
answer = 0
while left < len(ab) and right >= 0:
	temp = ab[left] + cd[right]
	if temp > 0:
		right -= 1
	elif temp < 0:
		left += 1
	else:
		ab_left, ab_right = bisect.bisect_left(ab, ab[left]), bisect.bisect_right(ab, ab[left])
		cd_left, cd_right = bisect.bisect_left(cd, cd[right]), bisect.bisect_right(cd, cd[right])
		answer += (ab_right - ab_left) * (cd_right - cd_left)
		left = ab_right
		right = cd_left - 1
print(answer)
