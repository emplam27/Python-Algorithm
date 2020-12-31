import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline


def BFS():
    queue = deque()
    visited = set()
    queue.append((N, 0))
    visited.add(N)

    while queue:
        location, value = queue.popleft()
        # 종료조건
        if (location - 1) == K or (location + 1) == K or (location * 2) == K:
            print(value + 1)
            exit()

        # 현재위치가 K를 넘어갔다면 *2, +1은 할 필요가 없음
        if location > K:
            if (location - 1) not in visited:
                queue.append((location - 1, value + 1))
                visited.add(location - 1)

        # 현재위치가 K를 넘어가지 않았다면 모두 수행
        else:
            if (location * 2) not in visited:
                queue.append((location * 2, value + 1))
                visited.add(location * 2)
            if (location - 1) not in visited:
                queue.append((location - 1, value + 1))
                visited.add(location - 1)
            if (location + 1) not in visited:
                queue.append((location + 1, value + 1))
                visited.add(location + 1)


N, K = map(int, read().rstrip().split())
if N == K:
    print(0)
else:
    BFS()
