'''
사대의 수 M (1 ≤ M ≤ 100,000), 동물의 수 N (1 ≤ N ≤ 100,000), 사정거리 L (1 ≤ L ≤ 1,000,000,000)

동물을 순회하면서 해당 동물을 잡을 수 있는 사대가 있는지 확인한다.
사정거리에서 y값을 빼주고, 이분탐색을 이용하여 남은 사정거리 범위 안에 사대가 있는지 확인한다.
'''

import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

M, N, L = map(int, read().split())
shoot_place = sorted(list(map(int, read().split())))
animals = [list(map(int, read().split())) for _ in range(N)]

result = 0
for x, y in animals:
    shoot_range = L - y
    left, right = 0, M - 1
    while left <= right:
        mid = (left + right) // 2
        if x - shoot_range <= shoot_place[mid] <= x + shoot_range:
            result += 1
            break

        elif shoot_place[mid] < x - shoot_range:
            left = mid + 1
        else:
            right = mid - 1
print(result)
