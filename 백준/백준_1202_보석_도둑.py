import sys
from heapq import heappush, heappop

sys.stdin = open("input.txt", "r")
read = sys.stdin.readline

'''
보석을 보석의 무게 순서로 정렬, 가방을 무게순서로 정렬하여 작은 가방부터 검사
가방에 담을 수 있는 보석을 검사하여 무게기준 최대힙에 push
다 넣어주면 최댓값만 pop하여 결과값에 추가
'''


def solve():
    N, K = map(int, read().rstrip().split())
    jewelries = [list(map(int, read().rstrip().split())) for _ in range(N)]
    jewelries.sort(key=lambda x: x[0])
    bags = sorted([int(read().rstrip()) for _ in range(K)])
    candidate = []

    result = 0
    jewelry_index = 0
    for bag_weight in bags:
        while jewelry_index < N and jewelries[jewelry_index][0] <= bag_weight:
            heappush(candidate, (-jewelries[jewelry_index][1], jewelries[jewelry_index]))
            jewelry_index += 1
        if candidate:
            result += heappop(candidate)[1][1]

    print(result)


solve()
