s = input()
c_arr = [0 for _ in range(26)]
for c in s:
    c_arr[ord(c) - 65] += 1
odd_c = 0
center = ""
palindrome = ""
for i in range(26):
    if c_arr[i] % 2 == 1:
        odd_c += 1
        center += chr(i + 65)
    palindrome += chr(i + 65) * (c_arr[i] // 2)
if odd_c > 1:
    print("I'm Sorry Hansoo")
else:
    print(palindrome + center + palindrome[::-1])