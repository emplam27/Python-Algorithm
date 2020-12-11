import sys

sys.stdin = open('input.txt', 'r')

nums = [int(sys.stdin.readline()) for _ in range(9)]
print(max(nums), nums.index(max(nums)) + 1)
