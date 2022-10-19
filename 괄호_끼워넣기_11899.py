s = input()
stack = []
cnt = 0
for c in s:
    if c == '(':
        stack.append(c)
    elif c == ')':
        if not stack:
            cnt += 1
        else:
            stack.pop()
print(cnt + len(stack))