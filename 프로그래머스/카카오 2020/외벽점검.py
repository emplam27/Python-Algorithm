def check_visited(n, weak, weak_idx, dist_value, weak_visited):
    time, value = 0, weak[weak_idx]
    while time <= dist_value:
        if value in weak and weak_visited[weak.index(value)] == 0:
            weak_visited[weak.index(value)] = 1
        value += 1
        if value == n:
            value = 0
        time += 1
    return weak_visited


def uncheck_visited(n, weak, weak_idx, dist_value, weak_visited):
    time, value = 0, weak[weak_idx]
    while time <= dist_value:
        if value in weak and weak_visited[weak.index(value)] == 1:
            weak_visited[weak.index(value)] = 0
        value += 1
        if value == n:
            value = 0
        time += 1
    return weak_visited


def check_outside(n, weak, dist, min_result, weak_visited, dist_selected):
    if 0 not in weak_visited:
        return dist_selected.count(1)

    for weak_idx in range(len(weak_visited)):
        if not weak_visited[weak_idx]:
            for dist_idx in range(len(dist_selected)):
                if not dist_selected[dist_idx]:
                    weak_visited = check_visited(n, weak, weak_idx, dist[dist_idx], weak_visited)
                    dist_selected[dist_idx] = 1
                    min_result = min(min_result, check_outside(n, weak, dist, min_result, weak_visited, dist_selected))
                    weak_visited = uncheck_visited(n, weak, weak_idx, dist[dist_idx], weak_visited)
                    dist_selected[dist_idx] = 0
    return min_result


def solution(n, weak, dist):
    answer = 0

    weak_visited = [0] * len(weak)
    dist_selected = [0] * len(dist)
    return check_outside(n, weak, dist, len(dist), weak_visited, dist_selected)


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
