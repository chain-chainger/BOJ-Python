import sys
input = sys.stdin.readline

word = input().rstrip().upper()
characters = list(set(word))
counts = []

for character in characters:
    counts.append(word.count(character))

if counts.count(max(counts)) > 1:
    print("?")
else:
    print(characters[counts.index(max(counts))])
