import sys
input = sys.stdin.readline

n = int(input())
answers = input().rstrip()
adrian = ['A', 'B', 'C']
bruno = ['B', 'A', 'B', 'C']
goran = ['C', 'C', 'A', 'A', 'B', 'B']
adrian_count = bruno_count = goran_count = 0
for i in range(n):
    if adrian[i % 3] == answers[i]:
        adrian_count += 1
    if bruno[i % 4] == answers[i]:
        bruno_count += 1
    if goran[i % 6] == answers[i]:
        goran_count += 1
max_count = max(adrian_count, bruno_count, goran_count)
print(max_count)
if max_count == adrian_count:
    print("Adrian")
if max_count == bruno_count:
    print("Bruno")
if max_count == goran_count:
    print("Goran")