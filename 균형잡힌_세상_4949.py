while True:
    s = input()
    if s == '.':
        break
    stack = []
    flag = True
    for c in s:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            if not stack or stack[-1] == '[':
                flag = False
                break
            else:
                stack.pop()
        elif c == ']':
            if not stack or stack[-1] == '(':
                flag = False
                break
            else:
                stack.pop()
    if flag and not stack:
        print("yes")
    else:
        print("no")