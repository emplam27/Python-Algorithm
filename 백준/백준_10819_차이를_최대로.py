import sys

sys.stdin = open('input.txt', 'r')

from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))
perm_list = list(permutations(nums, N))

max_result = 0
for perm_elem in perm_list:
    tmp_result = 0
    for index in range(N - 1):
        tmp_result += abs(perm_elem[index] - perm_elem[index + 1])
    max_result = max(max_result, tmp_result)
print(max_result)