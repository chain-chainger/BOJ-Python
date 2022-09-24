pkht = {'P':13, 'K':13, 'H':13, 'T':13}
s = input()
set_card = set()
for i in range(0, len(s), 3):
    if s[i:i+3] in set_card:
        print("GRESKA")
        exit(0)
    set_card.add(s[i:i+3])
    pkht[s[i]] -= 1
print(*pkht.values())