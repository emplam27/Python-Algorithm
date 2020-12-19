import sys
import heapq

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

N = int(read())
# left는 최대힙, right는 최소힙
mid, left, right = int(read()), [], []
print(mid)

for length in range(1, N):
    new_num = int(read())

    print('length', length, '=>', length + 1)

    # 길이가 짝수에서 홀수가 될 때
    if length % 2 == 0:
        # 새로운 숫자가 현재의 중간값보다 작아 left에 추가된다면 중간값은 그대로 유지
        if mid > new_num:
            heapq.heappush(left, (-new_num, new_num))
            print('left')
            print(mid)
        # 아니라면 새로운 숫자는 right에 추가되고, right의 최솟값이 mid가 됨
        # mid는 left에 추가됨
        else:
            heapq.heappush(left, (-mid, mid))
            heapq.heappush(right, new_num)
            mid = heapq.heappop(right)
            print('right')
            print(mid)

    # 길이가 홀수에서 짝수가 될 때
    else:
        # 새로운 숫자가 현재의 중간값보다 커 뒤쪽에 추가된다면 중간값은 그대로
        if mid < new_num:
            heapq.heappush(right, new_num)
            print('right')
            print(mid)
        else:
            # 아니라면 새로운 숫자는 left에 추가되고, left의 최댓값이 mid가 됨
            # mid는 right에 추가됨
            heapq.heappush(right, mid)
            heapq.heappush(left, (-new_num, new_num))
            mid = heapq.heappop(left)[1]
            print('left')
            print(mid)
    print(left, mid, right)

