import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

'''
이진탐색을 어떻게 활용하는 것이 좋을까?

공유기를 배치하는 것은 선형으로 검사한다. 선형검색말고 이진탐색으로는 불가능하다.
이진탐색은 '가장 이웃한 공유기 거리'를 결정할때 사용한다. 
이진탐색으로 공유기를 놓을 '가장 이웃한 공유기 거리'를 설정하고, 그 아상의 거리에 있는 집들만 공유기를 놓는다. 
놓은 공유기의 수가 적다면 최소거리를 줄이고, 많다면 최소거리를 늘린다. 
'''


def check_distance(distance):
    count, current_house = 1, houses[0]
    for house_index in range(1, N):
        if houses[house_index] - current_house >= distance:
            current_house = houses[house_index]
            count += 1
    return count


read = sys.stdin.readline
N, C = map(int, read().split())
houses = sorted([int(read()) for _ in range(N)])

result = 0
left, right = 1, houses[-1] - houses[0]
while left <= right:
    mid = (left + right) // 2
    result_count = check_distance(mid)
    if result_count >= C:
        left = mid + 1
        result = mid  # '가장 이웃한 공유기 거리'의 최댓값을 구하는 것이기 때문에 result를 해당 부분에서 갱신
    elif result_count <= C:
        right = mid - 1
print(result)
