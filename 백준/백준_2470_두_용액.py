import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

'''
이분탐색으로 찾아야 하는건 '두 특성값 합의 절댓값이 최소가 되는 특성값'

'''

N = int(read())
liquids = sorted(map(int, read().split()))
min_diff, result = float('inf'), []

for liquid in liquids:

    # 이분 탐색으로 찾아야 하는 값과 유사한 값의 index 찾기
    left, right = 0, N - 1
    mid = (left + right) // 2
    while left <= right and 0 <= mid < N:
        current_props = liquids[mid]

        if min_diff > abs(liquid + liquids[mid]):
            result = [liquid, liquids[mid]]
            min_diff = abs(liquid + liquids[mid])

            if liquid > 0:
                if abs(liquid) < abs(liquids[mid]):
                    mid += 1
                else:
                    mid -= 1
            else:
                if abs(liquid) < abs(liquids[mid]):
                    mid -= 1
                else:
                    mid += 1

        else:
            if liquid > 0:
                if abs(liquid) < abs(liquids[mid]):
                    mid = (mid + 1 + right) // 2
                else:
                    mid = (left + mid - 1) // 2
            else:
                if abs(liquid) < abs(liquids[mid]):
                    mid = (left + mid - 1) // 2
                else:
                    mid = (mid + 1 + right) // 2

print(*result)
