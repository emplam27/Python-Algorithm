import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline


def DFS(start):
    stack, result = list(), list()
    stack.append(start)
    visited = [0] * (N + 1)

    while stack:
        cur_node = stack.pop()
        if not visited[cur_node]:
            result.append(cur_node)
            visited[cur_node] = 1
            for next_node in range(N, 0, -1):
                if graph[cur_node][next_node] and not visited[next_node]:
                    stack.append(next_node)

    return result


def BFS(start):
    queue, result = deque(), list()
    queue.append(start)
    visited = [0] * (N + 1)

    while queue:
        cur_node = queue.popleft()
        if not visited[cur_node]:
            result.append(cur_node)
            visited[cur_node] = 1
            for next_node in range(1, N + 1):
                if graph[cur_node][next_node] and not visited[next_node]:
                    queue.append(next_node)

    return result


N, M, V = map(int, read().rstrip().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    i, j = list(map(int, read().rstrip().split()))
    graph[i][j], graph[j][i] = 1, 1

print(*DFS(V))
print(*BFS(V))
