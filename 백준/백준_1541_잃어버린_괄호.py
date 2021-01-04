import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline


nums = list(input().split('-'))
for index, value in enumerate(nums):
    nums[index] = sum(map(int, value.split('+')))
print(-sum(nums) + 2 * nums[0])