import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    room_floor = N % H
    room_number = N // H + 1
    
    if room_floor == 0:
        room_floor = H
        room_number -= 1
    
    print(room_floor * 100 + room_number)
    