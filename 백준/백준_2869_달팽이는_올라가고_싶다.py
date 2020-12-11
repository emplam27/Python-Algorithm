import sys

sys.stdin = open('input.txt', 'r')

import math

A, B, V = map(int, input().split())
print(math.ceil((V - A) / (A - B)) + 1)