import sys

sys.stdin = open("input.txt", "r")


# def dfs(x):
#     rec.append(str(x))
#     for v in line2[x]:
#         rec2[v] -= 1
#         if rec2[v] == 0:
#             dfs(v)
#
#
# for i in range(1, 11):
#     V, E = map(int, input().split())
#     line = list(map(int, input().split()))
#     line2 = [[] for _ in range(V + 1)]
#     rec = []
#     rec2 = [0] * (V + 1)
#     rec3 = []
#     for j in range(0, len(line), 2):
#         line2[line[j]].append(line[j + 1])
#     for j in range(1, V + 1):
#         for k in range(1, V + 1):
#             rec2[j] += line2[k].count(j)
#         if rec2[j] == 0:
#             rec3.append(j)
#     print(rec2)
#     for j in rec3:
#         dfs(j)
#     print('#{} {}'.format(i, ' '.join(rec)))





def DFS(N):
    result.append(str(N))
    for i in range(V + 1):
        if mat[N][i] == 1:
            count[i] -= 1
            if count[i] == 0:
                DFS(i)


for t in range(1, 11):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    rule = []
    for i in range(E):
        rule.append([arr[2 * i], arr[2 * i + 1]])

    # 시작점인 숫자들 조사
    # 후행 노드 카운트를 만든다. 후행노트 카운트에 없는 숫자들은 무조건 맨처음 수행하는 노드가 된다.
    count = [0] * (V + 1)
    for i in range(E):
        count[rule[i][1]] += 1

    initial_num = []
    for i in range(1, V + 1):
        for j in range(E):
            if count[i] == 0:
                initial_num.append(i)
                break

    # 선행작업 -> 후행작업 메트릭스에서 후행작업을 탐색할 수 있게 한다.
    mat = [[0] * (V + 1) for _ in range(V + 1)]
    for start, end in rule:
        mat[start][end] = 1

    result = []
    for initial in initial_num:
        DFS(initial)

    print('#{} {}'.format(t, ' '.join(result)))
