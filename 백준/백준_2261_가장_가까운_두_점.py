import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline


n = int(read().rstrip())
points = [list(map(int, read().rstrip().split())) for _ in range(n)]

print(points)


