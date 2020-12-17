import sys

sys.stdin = open('input.txt', 'r')


N, std_nums = int(input()), sorted(list(map(int, input().split())))
M, com_nums = int(input()), list(map(int, input().split()))

for com_value in com_nums:
    left, right = 0, N - 1
    while left <= right and 0 <= left < N and 0 <= right < N:
        mid = (left + right) // 2
        if std_nums[mid] < com_value:
            left = mid + 1
        elif std_nums[mid] > com_value:
            right = mid - 1
        else:
            print(1)
            break
    else:
        print(0)



