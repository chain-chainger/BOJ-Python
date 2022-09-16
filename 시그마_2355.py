a, b = map(int, input().split())
sum = (a + b) * (abs(a - b) + 1) // 2
print(sum)