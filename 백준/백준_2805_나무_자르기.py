import sys

sys.stdin = open('input.txt', 'r')


'''
1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000

각 배열은 해당 높이에서 잘랐을 때 얻을 수 있는 나무의 높이
얻고자 하는 나무의 양이 주어진다면 해당 부분을 넘는 최소 index를 찾은 후
필요한 나무의 높이만큼 높이를 (N - index) * (높이)만큼 내려서 높이의 최댓값을 찾는다.


'''

N, M = map(int, input().split())
woods = sorted(list(map(int, input().split())))

left, right = 0, woods[-1]
while left <= right:
    mid = (left + right) // 2

    wood_sum = 0
    for wood in woods:
        wood_sum += (wood - mid) if wood > mid else 0

    if wood_sum > M:
        left = mid + 1
    elif wood_sum < M:
        right = mid - 1
    else:
        print(mid)
        exit()
print(min(left, right))

# # 해당 높이에서 자르면 얻을 수 있는 나무의 양
# gain_stack = 0
# for index in range(N, 0, -1):
#     tmp = woods[index] - woods[index - 1]
#     woods[index] = [woods[index], gain_stack]
#     gain_stack += tmp
# woods[0] = [0, woods[-1][0]]
# print(N, M, woods)
#
# # 해당 높이를 넘는 최소 index 구하기
# left, right = 0, N
# while left <= right:
#     mid = (left + right) // 2
#     if woods[mid + 1][1] <= M <= woods[mid][1]:
#         break
#     elif woods[mid][1] == M:
#         print(woods[mid][0])
#         exit()
#     elif woods[mid][1] > M:
#         left = mid + 1
#     else:
#         right = mid - 1
# print(mid)
#
# result = woods[mid][0] + (woods[mid][1] - M) // (N - 1)
#
