s = input()
s = s.replace("pi", " ")
s = s.replace("ka", " ")
s = s.replace("chu", " ")
s = s.replace(" ","")
if len(s):
    print("NO")
else:
    print("YES")