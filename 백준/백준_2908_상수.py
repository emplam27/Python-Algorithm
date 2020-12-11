import sys

sys.stdin = open('input.txt', 'r')

A, B = input().split()
print(max(A[::-1], B[::-1]))