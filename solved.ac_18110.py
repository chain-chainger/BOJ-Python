import sys
input = sys.stdin.readline

def custom_round(target):
    if target - int(target) >= 0.5:
        return int(target) + 1
    return int(target)

n = int(input())

if n == 0:
    print(0)
else:
    scores = [int(input()) for _ in range(n)]
    except_len = custom_round(n * 0.15)
    target_scores = sorted(scores)[except_len:n - except_len]

    print(custom_round(sum(target_scores) / len(target_scores)))