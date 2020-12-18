import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline


N = int(read())
towers = list(map(int, read().split()))

stack = []
result = [0] * N
for index in range(N - 1, -1, -1):
    tower = towers[index]
    if not stack:
        stack.append([tower, index])
        continue

    while stack and tower > stack[-1][0]:
        tmp_tower = stack.pop()
        result[tmp_tower[1]] = index + 1
    stack.append([tower, index])
print(*result)
