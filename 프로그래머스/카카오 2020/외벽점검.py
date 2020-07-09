def solution(n, weak, dist):
    def check_visited(weak_idx, dist_value):

        origin_weak_value = weak[weak_idx]
        weak_visited[weak_idx] = 1
        visited_index = []

        for _ in range(len(weak)):
            weak_idx += 1
            if weak_idx < len(weak):
                if not weak_visited[weak_idx] and weak[weak_idx] <= origin_weak_value + dist_value:
                    weak_visited[weak_idx] = 1
                    visited_index.append(weak_idx)
                else:
                    break
            else:
                if not weak_visited[weak_idx - len(weak)] and weak[
                    weak_idx - len(weak)] <= origin_weak_value + dist_value - (n - 1):
                    weak_visited[weak_idx - len(weak)] = 1
                    visited_index.append(weak_idx - len(weak))
                else:
                    break

        return weak_visited, visited_index

    def uncheck_visited(visited_index):
        for i in visited_index:
            weak_visited[i] = 0
        return weak_visited

    def check_outside(min_result, weak_visited):

        if dist_selected.count(1) >= min_result:
            return min_result

        if 0 not in weak_visited:
            return dist_selected.count(1)

        for weak_idx in range(len(weak)):
            if not weak_visited[weak_idx]:
                for dist_idx in range(len(dist)):
                    if not dist_selected[dist_idx]:
                        weak_visited, visited_index = check_visited(weak_idx, dist[dist_idx])
                        dist_selected[dist_idx] = 1
                        min_result = min(min_result, check_outside(min_result, weak_visited))
                        weak_visited = uncheck_visited(weak_visited)
                        dist_selected[dist_idx] = 0
        return min_result

    weak_visited = [0] * len(weak)
    dist_selected = [0] * len(dist)
    min_result = check_outside(len(dist) + 1, weak_visited)
    if min_result == len(dist) + 1:
        return -1
    else:
        return min_result


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
