import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    start, end = map(int, input().split())
    visited = [0] * (V + 1)

    # 연결정보 배열
    connected = [[0] * (V + 1) for _ in range(V + 1)]
    for i, j in arr:
        connected[i][j], connected[j][i] = 1, 1

    # 검사
    result = 0
    queue = [(start, 0)]
    while len(queue) > 0:
        idx, m = queue.pop(0)
        visited[idx] = 1
        for d in range(V + 1):
            if connected[idx][d] == 1 and visited[d] == 0:
                if d == end:
                    result = m + 1
                    break
                else:
                    queue.append((d, m + 1))
        if result != 0:
            break

    print('#%d' %t, result)