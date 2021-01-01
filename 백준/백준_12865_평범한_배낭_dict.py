import sys

read = sys.stdin.readline

N, K = map(int, read().rstrip().split())
memo = dict({0: 0})
for _ in range(N):
    W, V = map(int, read().rstrip().split())
    tmp_memo = dict()
    for weight, value in memo.items():
        if weight + W <= K:
            tmp_memo[weight + W] = max(memo.get(weight + W, 0), memo.get(weight, 0) + V)
    memo.update(tmp_memo)

max_result = 0
for value in memo.values():
    if max_result < value:
        max_result = value
print(max_result)
