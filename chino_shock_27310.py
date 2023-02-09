emoji = input()
colon_count, underbar_count = 0, 0
for c in emoji:
    if c == ':':
        colon_count += 1
    elif c == '_':
        underbar_count += 1
print(len(emoji) + colon_count + (underbar_count * 5))