import sys

sys.stdin = open('input.txt', 'r')

N = int(input())
prev_tile, cur_tile = 1, 2
if N == 1:
    print(1)
    exit()
for _ in range(N - 2):
    tmp = (cur_tile + prev_tile) % 15746
    prev_tile = cur_tile
    cur_tile = tmp

print(cur_tile)
 