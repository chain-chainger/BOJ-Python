import sys
input = sys.stdin.readline

N = int(input())
current_number = 1
add_number = 0
answer = 1

while True:
    if current_number >= N:
        print(answer)
        break
    add_number = add_number + 6
    current_number += add_number
    answer += 1
    