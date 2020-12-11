import sys

sys.stdin = open('input.txt', 'r')


def bubble_sort(arr):
    for index in range(len(arr) - 1):
        for i in range(len(arr) - index - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


N = int(input())
nums = [int(input()) for _ in range(N)]
bubble_sort(nums)
for i in nums:
    print(i)
