import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline


N = int(read())
bars = [int(input()) for _ in range(N)]

result = [bars[-1]]
for i in range(N - 2, -1, -1):
    if result[-1] < bars[i]:
        result.append(bars[i])

print(len(result))
