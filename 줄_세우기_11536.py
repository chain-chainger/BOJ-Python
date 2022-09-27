n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
if arr == sorted(arr):
    print("INCREASING")
elif arr == sorted(arr, reverse=True):
    print("DECREASING")
else:
    print("NEITHER")