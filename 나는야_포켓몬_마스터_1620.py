import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pocketmon_dict = {}

for i in range(1, N + 1):
    pocketmon_name = input().rstrip()
    pocketmon_dict[i] = pocketmon_name
    pocketmon_dict[pocketmon_name] = i

for _ in range(M):
    input_data = input().rstrip()
    if input_data.isnumeric():
        print(pocketmon_dict[int(input_data)])
    else:
        print(pocketmon_dict[input_data])