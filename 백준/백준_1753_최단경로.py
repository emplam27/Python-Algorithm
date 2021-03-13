import sys
from heapq import heappush, heappop

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline


def solve():
    V, E = map(int, read().rstrip().split())
    K = int(read().rstrip())
    INF = sys.maxsize
    dp, heap, graph = [INF] * (V + 1), list(), [list() for _ in range(V + 1)]
    for _ in range(E):
        u, v, w = map(int, read().rstrip().split())
        graph[u].append([w, v])

    dp[K] = 0
    heappush(heap, [0, K])
    while heap:
        curr_val, curr_node = heappop(heap)
        if dp[curr_node] < curr_val:
            continue

        for next_val, next_node in graph[curr_node]:
            next_val += curr_val
            if next_val < dp[next_node]:
                dp[next_node] = next_val
                heappush(heap, [next_val, next_node])

    for i in range(V):
        print("INF" if dp[i + 1] == INF else dp[i + 1])
    return


solve()
