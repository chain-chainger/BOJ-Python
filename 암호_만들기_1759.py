import sys
input = sys.stdin.readline

def check(password):
    count_vowel, count_consonant = 0, 0
    for character in password:
        if character in vowels:
            count_vowel += 1
        else:
            count_consonant += 1
    if count_vowel >= 1 and count_consonant >= 2:
        return True
    return False

def dfs(start):
    if len(password) == l:
            if check(password):
                print(''.join(password))
                return
    for i in range(start, c):
        password.append(arr[i])
        dfs(i + 1)
        password.pop()

vowels = ['a', 'e', 'i', 'o', 'u']
l, c = map(int, input().split())
arr = list(input().split())
arr.sort()
password = []
dfs(0)