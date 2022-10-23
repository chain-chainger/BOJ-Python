n = int(input())
files = {}
for _ in range(n):
    file = input().split('.')[1]
    if file not in files:
        files[file] = 1
    else:
        files[file] += 1
files = sorted(files.items())
for file, cnt in files:
    print(file, cnt)