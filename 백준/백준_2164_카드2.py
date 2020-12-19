import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

N = int(read())
queue = deque([i for i in range(1, N + 1)])

while len(queue) > 1:
    queue.popleft()
    if len(queue) == 1:
        break
    queue.append(queue.popleft())
print(*queue)
