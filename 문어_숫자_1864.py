import sys
input = sys.stdin.readline

dic = {"-":0, "\\":1, "(":2, "@":3, "?":4, ">":5, "&":6, "%":7, "/": -1}
while True:
    octopus_number = input().rstrip()
    if octopus_number == "#":
        break
    answer = 0
    for i in range(len(octopus_number)):
        answer += dic[octopus_number[i]] * 8 ** (len(octopus_number) - i - 1)
    print(answer)