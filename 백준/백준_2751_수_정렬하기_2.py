import sys

sys.stdin = open('input.txt', 'r')

import sys


# def merge_sort(arr):
#
#     if len(arr) <= 2:
#         if len(arr) == 2:
#             if arr[0] > arr[1]:
#                 arr[0], arr[1] = arr[1], arr[0]
#         return arr
#
#     arr_1 = merge_sort(arr[:len(arr) // 2])
#     arr_2 = merge_sort(arr[len(arr) // 2:])
#
#     new_arr = []
#     while arr_1 and arr_2:
#         if arr_1[0] < arr_2[0]:
#             new_arr.append(arr_1.pop(0))
#         else:
#             new_arr.append(arr_2.pop(0))
#     if arr_1:
#         new_arr.extend(arr_1)
#     else:
#         new_arr.extend(arr_2)
#
#     return new_arr
#
#
# N = int(sys.stdin.readline())
# nums = [int(sys.stdin.readline()) for _ in range(N)]
# nums = merge_sort(nums)
# for i in nums:
#     print(i)


N = int(sys.stdin.readline())
nums = [0] * 10001
for _ in range(N):
    nums[int(sys.stdin.readline())] += 1

for index, value in enumerate(nums):
    if value:
        for _ in range(value):
            print(index)

