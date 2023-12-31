import sys
input = sys.stdin.readline

while True:
	triangle = list(map(int, input().split()))
	if triangle.count(0) == 3:
		break
	triangle.sort()
	if triangle[2] >= triangle[0] + triangle[1]:
		print("Invalid")
	elif triangle[2] == triangle[1] == triangle[0]:
		print("Equilateral")
	elif triangle[2] == triangle[1] or triangle[2] == triangle[0] or triangle[1] == triangle[0]:
		print("Isosceles")
	else:
		print("Scalene")
