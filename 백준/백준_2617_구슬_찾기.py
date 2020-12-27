import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline


N, M = map(int, read().rstrip().split())
marbles = [list(map(int, read().rstrip().split())) for _ in range(M)]

print(marbles)