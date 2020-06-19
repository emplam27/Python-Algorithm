import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    submat = list()

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                delta_i = 1
                delta_j = 1
                while arr[i + delta_i][j] != 0:
                    delta_i += 1
                while arr[i][j + delta_j] != 0:
                    delta_j += 1

                submat.append([delta_i * delta_j, delta_i, delta_j])

                for k in range(delta_i):
                    for l in range(delta_j):
                        arr[i + k][j + l] = 0


    len_submat = len(submat)
    submat_str = ''
    max_size = 0
    for i in range(len_submat):
        if submat[i][0] > max_size:
            max_size = submat[i][0]

    sort_submat = []
    for i in range(max_size + 1):
        tmp_list = []
        for j in range(len_submat):
            if i == submat[j][0]:
                tmp_list.append(submat[j])

        if len(tmp_list) == 1:
            sort_submat.append(tmp_list[0])

        else:
            while len(tmp_list) > 0:
                min_delta_i = 101
                min_delta_idx = 0
                for k in range(len(tmp_list)):
                    if tmp_list[k][1] < min_delta_i:
                        min_delta_i = tmp_list[k][1]
                        min_delta_idx = k
                sort_submat.append(tmp_list.pop(min_delta_idx))

    print('#%d' % t, len_submat, end=' ')
    for i in range(len_submat):
        print(sort_submat[i][1], sort_submat[i][2], end=' ')
    print()
