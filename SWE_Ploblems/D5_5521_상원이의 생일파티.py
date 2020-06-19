import sys
sys.stdin = open("input.txt", "r")


from collections import deque


for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    friends = [list(map(int, input().split())) for _ in range(M)]

    relationship = [[0] * (N + 1) for _ in range(N + 1)]
    for friend in friends:
        relationship[friend[0]][friend[1]] = 1
        relationship[friend[1]][friend[0]] = 1

    result = 0
    visited = [0] * (N + 1)
    queue = deque()
    queue.append([1, 0])
    visited[1] = 1
    while queue:
        value, count = queue.popleft()
        if count < 2:
            for i in range(1, N + 1):
                if relationship[value][i] == 1 and visited[i] == 0:
                    visited[i] = 1
                    result += 1
                    queue.append([i, count + 1])


    print('#%d' %t, result)
