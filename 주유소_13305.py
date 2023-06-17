import sys
input = sys.stdin.readline

n = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))
cost = 0
price = prices[0]
for i in range(n - 1):
    if prices[i] < price:
        price = prices[i]
    cost += price * distances[i]
print(cost)
