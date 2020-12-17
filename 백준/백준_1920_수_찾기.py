import sys

sys.stdin = open('input.txt', 'r')


N, std_nums = int(input()), set(map(int, input().split()))
M, com_nums = int(input()), list(map(int, input().split()))

for _, value in enumerate(com_nums):
    if value in std_nums:
        print(1)
    else:
        print(0)