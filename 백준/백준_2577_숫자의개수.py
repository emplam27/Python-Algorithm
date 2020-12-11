import sys

sys.stdin = open('input.txt', 'r')

A, B, C = int(input()), int(input()), int(input())
results = [0] * 10
for number in str(A * B * C):
    results[int(number)] += 1
for result in results:
    print(result)