import sys

sys.stdin = open("15649_input.txt", "r")

N, M = map(int, input().split())


from itertools import combinations

items = []

for i in range(N):
    items.append(i+1)

print(list(combinations(items, 2)))


# selected = [0] * N
# count1 = 0
#
# def combination(idx, count1):
#
#     if idx == N:
#         if count1 == M:
#             for i in range(N):
#                 if selected[i] == 1:
#                     print(i + 1, end=' ')
#             print()
#         return
#
#
#     if count1 > M:
#         return
#
#     selected[idx] = 1
#     count1 += 1
#     combination(idx + 1, count1)
#     selected[idx] = 0
#     count1 -= 1
#     combination(idx + 1, count1)
#
#
# combination(0, 0)



