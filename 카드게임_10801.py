import sys
input = sys.stdin.readline

a_cards = list(map(int, input().split()))
b_cards = list(map(int, input().split()))
a_count, b_count = 0, 0
for i in range(10):
    if a_cards[i] > b_cards[i]:
        a_count += 1
    elif b_cards[i] > a_cards[i]:
        b_count += 1
if a_count > b_count:
    print("A")
elif b_count > a_count:
    print("B")
else:
    print("D")