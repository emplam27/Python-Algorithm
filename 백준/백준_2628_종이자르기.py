import sys

sys.stdin = open('input.txt', 'r')


W, H = map(int, input().split())
N = int(input())

cuts = [list(map(int, input().split())) for _ in range(N)]
horizontal, vertical = [0, W], [0, H]
for cut in cuts:
    if cut[0] == 1:
        horizontal.append(cut[1])
    else:
        vertical.append(cut[1])
horizontal.sort(reverse=True)
vertical.sort(reverse=True)

max_width, max_height = 0, 0
for index in range(len(horizontal) - 1):
    max_width = max(max_width, horizontal[index] - horizontal[index + 1])
for index in range(len(vertical) - 1):
    max_height = max(max_height, vertical[index] - vertical[index + 1])

print(max_width * max_height)
