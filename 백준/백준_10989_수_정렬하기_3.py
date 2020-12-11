import sys

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
nums = [0] * 10001
for _ in range(N):
    nums[int(sys.stdin.readline())] += 1

for index, value in enumerate(nums):
    if value:
        for _ in range(value):
            print(index)
