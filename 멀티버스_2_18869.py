import sys
input = sys.stdin.readline

m, n = map(int, input().split())
dictionary = {}
for _ in range(m):
    planets = list(map(int, input().split()))
    sorted_planets = sorted(list(set(planets)))
    ranks = {sorted_planets[i]:i for i in range(len(sorted_planets))}
    key = str([ranks[planet] for planet in planets])
    dictionary[key] = dictionary.get(key, 0) + 1
print(sum(map(lambda x:x * (x - 1) // 2, dictionary.values())))
