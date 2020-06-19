import sys

sys.stdin = open('input.txt', 'r')


# def powerset(idx, selected):
#     if idx == N:
#         sum_num = 0
#         for i in range(N):
#             if selected[i] == 1:
#                 sum_num += arr[i]
#         if sum_num not in score_list:
#             score_list.append(sum_num)
#         return
#
#     selected[idx] = 1
#     powerset(idx + 1, selected)
#     selected[idx] = 0
#     powerset(idx + 1, selected)



T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    a = sum(arr) + 1
    selected = [0] * a
    selected_list = []
    selected[0] = 1

    for i in arr:
        selected_list = []
        for j in range(a):
            if selected[j] == 1:
                selected_list.append(i + j)
        for k in selected_list:
            selected[k] = 1

    print('#%d' % t, selected.count(1))