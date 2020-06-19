import sys

sys.stdin = open('../SWE_Ploblems/input2.txt', 'r')

for t in range(1, int(input()) + 1):
    N = int(input())
    atom = [list(map(int, input().split())) for _ in range(N)]
    dy, dx = [0.5, -0.5, 0, 0], [0, 0, -0.5, 0.5]


    selected = [0] * N
    for i in range(N):
        tmp = []
        for j in range(i + 1, N):
            if selected[j] == 0:
                if atom[i][2] == 0 or atom[i][2] == 1:
                    tmp.append((atom[i][1], i))
                    if  atom[i][0] == atom[j][0]:
                        if atom[j][2] == 0 or atom[j][2] == 1:
                            tmp.append((atom[j][1], j))
                elif atom[i][2] == 2 or atom[i][2] == 3:
                    tmp.append((atom[i][1], i))
                    if  atom[i][1] == atom[j][1]:
                        if atom[j][2] == 2 or atom[j][2] == 3:
                            tmp.append((atom[j][0], j))
        # tmp = 한줄의 정보.
        if len(tmp) > 0:
            selected[i] = 1
            for k in range(len(tmp)):




    # move = list()
    # result = 0
    # while len(atom) > 0:
    #     move = []
    #     for x, y, c, k in atom:
    #         nx, ny = x + dx[c], y + dy[c]
    #         if -1000 <= nx <= 1000 and -1000 <= ny <= 1000:
    #             move.append([nx, ny, c, k])
    #
    #     atom = []
    #     visited = [0] * len(move)
    #     tmp, tmp_list = (0, 0), list()
    #     for i in range(len(move)):
    #         if visited[i] == 0:
    #             tmp, tmp_list = (move[i][0], move[i][1]), [move[i]]
    #             visited[i] = 1
    #             for j in range(i + 1, len(move)):
    #                 if tmp == (move[j][0], move[j][1]) and visited[j] == 0:
    #                     tmp_list.append(move[j])
    #                     visited[j] = 1
    #             if len(tmp_list) > 1:
    #                 for k in range(len(tmp_list)):
    #                     result += tmp_list[k][3]
    #             else:
    #                 atom.append(tmp_list[0])

    print('#%d' %t, result)