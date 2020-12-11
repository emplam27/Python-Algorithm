import sys

sys.stdin = open('input.txt', 'r')

x, y, w, h = map(int, sys.stdin.readline().split())
print(min(abs(x), abs(y), abs(w - x), abs(h - y)))
