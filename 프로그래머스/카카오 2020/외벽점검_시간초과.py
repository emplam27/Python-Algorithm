def check_visited(n, weak, weak_idx, dist_value, weak_visited):
    time = 0
    weak_value = weak[weak_idx]
    visited_index = []
    while time <= dist_value:
        if weak_value in weak:
            tmp_index = weak.index(weak_value)
            if weak_visited[tmp_index] == 0:
                weak_visited[tmp_index] = 1
                visited_index.append(tmp_index)
        weak_value += 1
        if weak_value == n:
            weak_value = 0
        time += 1
    return weak_visited, visited_index


def uncheck_visited(weak_visited, visited_index):
    for i in visited_index:
        weak_visited[i] = 0
    return weak_visited


def check_outside(n, weak, dist, min_result, weak_visited, dist_selected):
    if dist_selected.count(1) >= min_result:
        return min_result

    if 0 not in weak_visited:
        return dist_selected.count(1)

    for weak_idx in range(len(weak)):
        if not weak_visited[weak_idx]:
            for dist_idx in range(len(dist)):
                if not dist_selected[dist_idx]:
                    weak_visited, visited_index = check_visited(n, weak, weak_idx, dist[dist_idx], weak_visited)
                    dist_selected[dist_idx] = 1
                    min_result = min(min_result, check_outside(n, weak, dist, min_result, weak_visited, dist_selected))
                    weak_visited = uncheck_visited(weak_visited, visited_index)
                    dist_selected[dist_idx] = 0
    return min_result


def solution(n, weak, dist):
    weak_visited = [0] * len(weak)
    dist_selected = [0] * len(dist)
    return check_outside(n, weak, dist, len(dist), weak_visited, dist_selected)


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
