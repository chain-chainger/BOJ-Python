import sys
input = sys.stdin.readline

def solve():
    nums = sorted(list(map(int, input().split())))
    if len(set(nums)) == 1:
        return nums[0] * 5000 + 50000
    if len(set(nums)) == 2:
        if nums[1] == nums[2]:
            return nums[1] * 1000 + 10000
        else:
            return (nums[1] + nums[2]) * 500 + 2000
    for i in range(3):
        if nums[i] == nums[i + 1]:
            return nums[i] * 100 + 1000
    return nums[-1] * 100

answer = 0
n = int(input())
for _ in range(n):
    temp_answer = solve()
    if temp_answer > answer:
        answer = temp_answer
print(answer)