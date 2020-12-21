import sys
from heapq import heappush, heappop
from collections import deque

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

'''
모든 좌표들을 (작은좌표(A), 큰좌표(B)) 순서대로 바꿔준 뒤 정렬한다. 
정렬할때 A를 기준으로 B가 더 작은 요소가 앞으로 오게 정렬한다.

이후 A_location, B_location, is_possible을 만들어 준다.
A_locations은 A기준 최소힙. 가장 작은값부터 pop하여 current_location을 갱신 
B_locations은 B기준 최소힙. is_possible안에 들어갈 수 있는 영역을 pop하여 is_possible에 넣어줌 
is_possible은 set(). current_location의 A부터 A + D 사이에 들어오는 location들이 저장 

<검사>
1. B - A의 길이가 D 이상이면 pass 
2-1. is_possble이 비어있다면 A_location에서 pop하여 넣어주기
2-2. is_possible의 가장 앞 영역의 A와 A + D 사이에 영역이 들어올 수 있다면 pop하여 is possible에 넣어주기
3. B_location에서 current_location의 A와 A + D 안에 들어올 수 있는 영역을 모두 pop 하여 넣어주기
4. 모두 넣어주었다면 결과값을 갱신하고 is_possible에서 current_location을 빼주기
'''

N = int(read())
locations = [list(map(int, read().split())) for _ in range(N)]
D = int(read())

# (집 좌표, 사무실 좌표)를 앞쪽에 항상 작은 좌표가 오도록 바꿔줌
A_location, B_location = [], []
for location in locations:
    if location[0] > location[1]:
        location[0], location[1] = location[1], location[0]
    heappush(A_location, (location[0], location))
    heappush(B_location, (location[1], location))
print(A_location)
print(B_location)

is_possible = set()
index, result = 0, 0
for _ in range(N):
    current_location = heappop(A_location)[1]

    # 영역의 길이가 D를 넘어가면 continue
    if current_location[1] - current_location[0] > D:
        continue

    # is_possible이 비어있다면 추가
    elif not is_possible:
        is_possible.add(current_location)
        result = max(result, len(is_possible))
        continue

    # B_location에서 is_possible안에 들어올 수 있는 영역들을 골라 추가
    # else:
    #     is_possible.add(current_location)
    #
    #     while True:
    #         if current_location[0] > B_location[0][1][0]:
    #
    #         if current_location[0] <= B_location[0][1][0] and B_location[0][1][1] <= current_location[1]:
    #             tmp = heappop(B_location)
    #
    #
    #     if is_possible[0][0] <= locations[index][0] and locations[index][1] <= is_possible[0][0] + D:
    #         is_possible.append(locations[index])
    #         result = max(result, len(is_possible))
    #
    #     # is_possible안에 들어올 수 없다면 pop후 append
    #     else:
    #         is_possible.popleft()
    #         continue

print(result)














