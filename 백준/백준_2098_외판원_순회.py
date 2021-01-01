import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

N = int(read().rstrip())
board = [list(map(int, read().rstrip().split())) for _ in range(N)]

print(board)

