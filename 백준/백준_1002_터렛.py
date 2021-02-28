import sys

sys.stdin = open("input.txt", "r")
read = sys.stdin.readline


def solve():
    x1, y1, r1, x2, y2, r2 = map(int, read().rstrip().split())
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            return -1
        else:
            return 0

    d = ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)
    if d > r1 + r2:
        return 0
    if d == r1 + r2:
        return 1
    if d == abs(r1 - r2):
        return 1
    if d < abs(r1 - r2):
        return 0
    return 2


T = int(read())
for _ in range(T):
    print(solve())
