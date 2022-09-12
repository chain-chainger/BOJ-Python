while True:
    n = int(input())
    if n == 0:
        break
    arr = []
    arr_l = []
    for i in range(n):
        s = input()
        arr.append(s)
        arr_l.append(s.lower())
    print(arr[arr_l.index(min(arr_l))])