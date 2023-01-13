import sys
input = sys.stdin.readline

print_zero = [1, 0 , 1]
print_one = [0, 1, 1]
for i in range(3, 41):
    print_zero.append(print_zero[i-1] + print_zero[i-2])
    print_one.append(print_one[i-1] + print_one[i-2])
t = int(input())
for _ in range(t):
    n = int(input())
    print(print_zero[n], print_one[n])