import sys
input = sys.stdin.readline

while True:
	line = input().rstrip()
	if line == "EOI":
		break
	if "nemo" in line.lower():
		print("Found")
	else:
		print("Missing")
