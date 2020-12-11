import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for _ in range(T):
    R, S = input().split()
    result = ''
    for char in S:
        result += char * int(R)
    print(result)