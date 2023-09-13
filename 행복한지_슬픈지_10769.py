import sys
input = sys.stdin.readline

line = input().rstrip()
happy_count = line.count(":-)")
sad_count = line.count(":-(")
if happy_count == 0 and sad_count == 0:
	print("none")
elif happy_count == sad_count:
	print("unsure")
elif happy_count > sad_count:
	print("happy")
else:
	print("sad")
