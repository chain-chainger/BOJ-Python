import sys
input = sys.stdin.readline

while True:
    sentence = input().rstrip()
    if sentence == "*":
        break
    is_pangram = True
    for alphabet in range(ord('a'), ord('z') + 1):
        if chr(alphabet) not in sentence:
            is_pangram = False
            break
    print("Y" if is_pangram else "N")