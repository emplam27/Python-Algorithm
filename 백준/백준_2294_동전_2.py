import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline


def BFS(queue):
    visited = set()
    while queue:
        value, count = queue.popleft()
        for i in range(N):
            tmp_value = value + coin_values[i]
            if tmp_value <= K and tmp_value not in visited:
                if tmp_value == K:
                    return count + 1
                queue.append((value + coin_values[i], count + 1))
                visited.add(tmp_value)

    return -1


N, K = map(int, read().rstrip().split())
coin_values = [int(read()) for _ in range(N)]
coins = deque([(value, 1) for value in coin_values])

print(BFS(coins))
