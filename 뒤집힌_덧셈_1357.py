import sys
input = sys.stdin.readline

X, Y = input().split()
X = X[::-1]
Y = Y[::-1]
answer = int(X) + int(Y)
answer = str(answer)[::-1]
print(int(answer))
