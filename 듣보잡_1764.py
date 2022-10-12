n, m = map(int, input().split())
n_list = [input() for _ in range(n)]
m_list = [input() for _ in range(m)]
overlap = set(n_list) & set(m_list)
print(len(overlap))
for name in sorted(overlap):
    print(name)