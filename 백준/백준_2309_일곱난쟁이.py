import sys

sys.stdin = open('input.txt', 'r')

from itertools import combinations

nums = sorted([int(input()) for _ in range(9)])
comb_list = list(combinations(nums, 7))
for comb in comb_list:
    if sum(comb) == 100:
        for num in comb:
            print(num)
        exit()