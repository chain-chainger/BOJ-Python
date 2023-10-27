import sys
innput = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))
answer = [0]

for element in sequence:
    if answer[-1] < element:
        answer.append(element)
    else:
        left = 0
        right = len(answer)
        while left < right:
            mid = (right + left) // 2
            if answer[mid] < element:
                left = mid + 1
            else:
                right = mid
        answer[right] = element
print(len(answer) - 1)