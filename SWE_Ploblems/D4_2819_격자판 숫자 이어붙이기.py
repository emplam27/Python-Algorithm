import sys

sys.stdin = open('input.txt', 'r')


def check(rs, cs, idxs, chars):
    global result_cnt
    queue.append([rs, cs, idxs, chars])

    while queue:
        r, c, idx, char = queue.pop(0)

        if idx == 7:
            if char not in visited:
                visited.add(char)
                result_cnt += 1
            continue

        for d in range(4):
            nr = r + dy[d]
            nc = c + dx[d]
            if 0 <= nr < 4 and 0 <= nc < 4:
                queue.append([nr, nc, idx + 1, char + arr[nr][nc]])


T = int(input())
for t in range(1, T + 1):
    arr = [list(input().split()) for _ in range(4)]
    dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

    queue = []
    visited = set()
    result_cnt = 0
    for i in range(4):
        for j in range(4):
            check(i, j, 1, arr[i][j])

    print('#%d' % t, result_cnt)
