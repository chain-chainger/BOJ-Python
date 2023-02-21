import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
count_supervisor = 0
for applicants in a:
    count_supervisor += 1
    applicants -= b
    if applicants > 0:
        count_supervisor += (applicants // c) + (applicants % c != 0)
print(count_supervisor)