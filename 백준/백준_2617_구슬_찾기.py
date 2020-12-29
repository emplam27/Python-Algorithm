import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

'''
본인보다 무겁거나 또는 가벼운 구슬의 수가 반을 넘어가면 절대 가운데가 될 수 없다.

방향성을 가진 그래프로 나타내보자. 무거운 순서를 방향으로 가지는 그래프, 가벼운 순서를 방향으로 가지는 그래프.
모든 구슬에 대해 검사하면서 가벼운 그래프에서는 가벼운 구슬, 무거운 그래프에서는 무거운 구슬의 갯수들을 뽑아낸다.
'''


def DFS(start_marble, graph):
    stack = [start_marble]
    visited = [0] * (N + 1)
    visited[start_marble] = 1
    count = 0
    while stack:
        cur_marble = stack.pop()
        if graph.get(cur_marble):
            for next_marble in graph[cur_marble]:
                if not visited[next_marble]:
                    stack.append(next_marble)
                    visited[next_marble] = 1
                    count += 1
    return count


N, M = map(int, read().rstrip().split())
marbles = [list(map(int, read().rstrip().split())) for _ in range(M)]

lighter_graph, heavier_graph = dict(), dict()
for heavier, lighter in marbles:
    lighter_graph[lighter] = lighter_graph.get(lighter, []) + [heavier]
    heavier_graph[heavier] = heavier_graph.get(heavier, []) + [lighter]

result = 0
for marble in range(1, N + 1):
    if lighter_graph.get(marble):
        l_count = DFS(marble, lighter_graph)
        if l_count >= (N // 2) + 1:
            result += 1
            continue
    if heavier_graph.get(marble):
        h_count = DFS(marble, heavier_graph)
        if h_count >= (N // 2) + 1:
            result += 1
print(result)
