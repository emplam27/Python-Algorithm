import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

N, K = map(int, read().rstrip().split())
items = [list(map(int, read().rstrip().split())) for _ in range(N)]
items.sort()
memo = [0] * (K + 1)
visited = [0] * (K + 1)
visited[0] = 1
for cur_weight, value in items:
    for index in range(K, -1, -1):
        if cur_weight + index <= K and visited[index]:
            if memo[cur_weight + index] < memo[index] + value:
                memo[cur_weight + index] = memo[index] + value
            visited[cur_weight + index] = 1
print(max(memo))
