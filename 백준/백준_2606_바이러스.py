import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline


def DFS(start):
    stack, result = list(), 0
    stack.append(start)
    visited = [0] * (N + 1)

    while stack:
        cur_node = stack.pop()
        visited[cur_node] = 1
        for next_node in range(N, 0, -1):
            if graph[cur_node][next_node] and not visited[next_node]:
                stack.append(next_node)
                result += 1
                visited[next_node] = 1

    return result


N = int(read())
M = int(read())
graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    i, j = list(map(int, read().rstrip().split()))
    graph[i][j], graph[j][i] = 1, 1

print(DFS(1))
