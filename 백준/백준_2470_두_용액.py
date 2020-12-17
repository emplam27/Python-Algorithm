import sys

sys.stdin = open('input.txt', 'r')

read = sys.stdin.readline
N = int(read().rstrip())
liquids = sorted(map(int, read().split()))
min_diff, result = float('inf'), []
# print(liquids)

for liquid in liquids:
    target_liquid_props = -liquid

    # 이분 탐색으로 찾아야 하는 값과 유사한 값의 index 찾기
    left, right = 0, N - 1
    while left <= right:
        mid = (left + right) // 2

        if liquids[mid] < target_liquid_props:
            left = mid + 1
        elif liquids[mid] > target_liquid_props:
            right = mid - 1
        else:
            break

    # 후보군 골라주기
    find_candidates = [liquids[mid]]
    if mid < N - 1:
        find_candidates.append(liquids[mid + 1])
    if mid > 0:
        find_candidates.append(liquids[mid - 1])
    if left < N:
        find_candidates.append(liquids[left])
    if right > N:
        find_candidates.append(liquids[right])

    # print(find_candidates)
    # print(liquid)
    # 후보군 중 특성값의 합이 0에 제일 가까운 경우 찾기
    property_diff = float('inf')
    for candidate in find_candidates:
        if property_diff > abs(liquid + candidate):
            property_diff = abs(liquid + candidate)
            target_liquid_props = candidate
        # print(candidate)
    # print(target_liquid_props)

    # 최솟값 갱신하기
    if min_diff > abs(liquid + target_liquid_props):
        min_diff = abs(liquid + target_liquid_props)
        result = [liquid, target_liquid_props]

print(*result)
