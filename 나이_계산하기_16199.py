import sys
input = sys.stdin.readline

year1, month1, day1 = map(int, input().split())
year2, month2, day2 = map(int, input().split())
age = year2 - year1
if month2 - month1 >= 0:
    if month2 - month1 == 0 and day2 - day1 < 0:
        print(age - 1)
    else:
        print(age)
else:
    print(age - 1)
print(age + 1)
print(age)