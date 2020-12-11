import sys

sys.stdin = open('input.txt', 'r')

from functools import reduce

N = int(input())
if N == 0:
    print(1)
else:
    print(reduce((lambda x, y: x * y), [x for x in range(1, N + 1)]))