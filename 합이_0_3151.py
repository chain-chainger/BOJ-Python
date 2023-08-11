import sys
input = sys.stdin.readline

def solve(start, end, goal):
    global answer
    max_index = n
    while start < end:
        temp = students[start] + students[end]
        if temp < goal:
            start += 1

        elif temp == goal:
            if students[start] == students[end]:
                answer += end - start

            else:
                if max_index > end:
                    max_index = end
                    while max_index >= 0 and students[max_index - 1] == students[end]:
                        max_index -= 1
                answer += end - max_index + 1
            start += 1
        else:
            end -= 1

n = int(input())
students = list(map(int, input().split()))
students.sort()
answer = 0
for i in range(n - 2):
    start = i + 1
    end = n - 1
    goal = -students[i]
    solve(start, end, goal)
print(answer)
