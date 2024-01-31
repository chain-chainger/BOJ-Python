import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sites = {}

for _ in range(n):
    site, password = input().rstrip().split()
    sites[site] = password

for _ in range(m):
    target_site = input().rstrip()
    print(sites[target_site])