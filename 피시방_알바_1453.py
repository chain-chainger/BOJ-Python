import sys
input = sys.stdin.readline

N = int(input())
costomers = list(map(int, input().split()))
print(len(costomers) - len(set(costomers)))
