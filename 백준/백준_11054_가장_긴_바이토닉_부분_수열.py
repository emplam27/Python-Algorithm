import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

'''
LIS를 정방향, 역방향으로 구하여 각 구간을 더했을 때 최댓값을 구함
'''


def solve():
    N = int(read().rstrip())
    nums = list(map(int, read().rstrip().split()))
    reversed_nums = list(reversed(nums))

    LIS, LDS = [1] * N, [1] * N
    for current_index in range(1, N):
        for before_index in range(current_index):
            if nums[before_index] < nums[current_index]:
                LIS[current_index] = max(LIS[current_index], LIS[before_index] + 1)

        for before_index in range(current_index):
            if reversed_nums[before_index] < reversed_nums[current_index]:
                LDS[current_index] = max(LDS[current_index], LDS[before_index] + 1)
    LDS.reverse()

    print(max(map(sum, zip(LIS, LDS))) - 1)


solve()
