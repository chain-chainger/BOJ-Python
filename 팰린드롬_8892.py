def solve():
    k = int(input())
    arr = [input() for _ in range(k)]
    len_arr = len(arr)
    for i in range(len_arr):
        for j in range(len_arr):
            if i == j:
                continue
            temp = arr[i] + arr[j]
            if temp == temp[::-1]:
                return temp
    return 0
    
t = int(input())
while t:
    res = solve()
    print(0)if res == 0 else print(res)
    t -= 1