expression = input().split('-')
nums = []
for num in expression:
    sum = 0
    temp = num.split('+')
    for num in temp:
        sum += int(num)
    nums.append(sum)
res = nums[0]
for i in range(1, len(nums)):
    res -= nums[i]
print(res)