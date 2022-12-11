numbers = list(map(int, input().split()))
abc = input()
res = []
numbers.sort()
for i in range(3):
    if abc[i] == 'A':
        res.append(numbers[0])
    elif abc[i] == 'B':
        res.append(numbers[1])
    else:
        res.append(numbers[2])
print(*res)