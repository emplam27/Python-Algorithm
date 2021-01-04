import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

N, K = map(int, read().rstrip().split())
coins = [int(read().rstrip()) for _ in range(N)]

result = 0
for coin in reversed(coins):
    share, rest = divmod(K, coin)
    if share:
        result += share
        K -= share * coin
    if not K:
        break

print(result)
