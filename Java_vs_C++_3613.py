def j_to_c(s):
    res = ""
    if s[0].isupper() or (not s.isalpha()):
        return "Error!"
    for i in range(len(s)):
        if s[i].isupper():
            res = res + '_' + s[i].lower()
        else:
            res += s[i]
    return res

def c_to_j(s):
    flag = False
    res = ""
    if s[0] == '_' or s[-1] == '_':
        return "Error!"
    for i in range(len(s)):
        if (not s[i].islower()) and s[i] != '_':
            return "Error!"
        if s[i] == '_':
            if s[i-1] == '_':
                return "Error!"
            flag = True
            continue
        if flag:
            res += s[i].upper()
            flag = False
        else:
            res += s[i]
    return res

s = input()
for i in range(len(s)):
    if s[i] == '_':
        res = c_to_j(s)
        break
    if s[i].isupper():
        res = j_to_c(s)
        break
    if i == len(s) - 1:
        res = j_to_c(s)
print(res)       
    