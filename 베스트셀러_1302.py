n = int(input())
books = {}
for _ in range(n):
    s = input()
    if s not in books:
        books[s] = 1
    else:
        books[s] += 1
max = max(books.values())
max_list = []
for s in books:
    if max == books[s]:
        max_list.append(s)
max_list.sort()
print(max_list[0])