import sys

sys.stdin = open('input.txt', 'r')


def make_path(index, path):
    global min_result

    if index == N:
        if costs[path[-1]][path[0]]:
            path = path + [path[0]]
            tmp_result = 0
            for path_order in range(len(path) - 1):
                tmp_result += costs[path[path_order]][path[path_order + 1]]
            min_result = min(min_result, tmp_result)
            return
        return

    for island in range(N):
        if not path:
            visited[island] = 1
            path.append(island)
            make_path(index + 1, path)
            visited[island] = 0
            path.pop()
        elif not visited[island] and costs[path[-1]][island]:
            visited[island] = 1
            path.append(island)
            make_path(index + 1, path)
            visited[island] = 0
            path.pop()


N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
visited, min_result = [0] * N, 2**31
make_path(0, [])

print(min_result)

