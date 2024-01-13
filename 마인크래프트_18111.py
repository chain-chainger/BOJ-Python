import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
world = []
for i in range(N):
    world.extend(map(int, input().split()))

total_block = sum(world) + B
answer = 0
time = [0] * 257

for height in range(257):
    if total_block - (height * N * M) < 0:
        continue
    
    count = 0
    for place in world:
        if place > height:
            count += (place - height) * 2
        else:
            count += height - place
    time[height] = count
    if count <= time[answer]:
        answer = height
        
print(time[answer], answer)
            