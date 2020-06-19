# 3시간
# 쉽게 생각하는 연습을 할 것.
# input값을 문제와 유사하게, 보기좋게 가공하는 방법 생각해볼것

import sys

sys.stdin = open('input2.txt', 'r')

for t in range(1, int(input()) + 1):
    M, A = map(int, input().split())
    move_A = [0] + list(map(int, input().split()))
    move_B = [0] + list(map(int, input().split()))
    direct = [[0, 0], [-1, 0], [0, 1], [1, 0], [0, -1]]  # 상우하좌
    BC = [list(map(int, input().split())) for _ in range(A)]

    time, result = 0, 0
    nA, nB = [1, 1], [10, 10]
    while time <= M:
        # 걸리는 기지국 판별
        BC_visit = [0] * A
        visit_A, visit_B = [(0, 9)], [(0, 9)]

        # 이동
        nA = [nA[0] + direct[move_A[time]][0], nA[1] + direct[move_A[time]][1]]
        nB = [nB[0] + direct[move_B[time]][0], nB[1] + direct[move_B[time]][1]]

        # 어느 기지국에 걸리는지 탐색
        for i in range(A):
            if abs(BC[i][0] - nA[1]) + abs(BC[i][1] - nA[0]) <= BC[i][2]:
                BC_visit[i] += 1
                visit_A.append((BC[i][3], i))
            if abs(BC[i][0] - nB[1]) + abs(BC[i][1] - nB[0]) <= BC[i][2]:
                BC_visit[i] += 1
                visit_B.append((BC[i][3], i))

        for _ in range(2):
            if len(visit_A) >= 2:
                for i in range(len(visit_A) - 1, 0, - 1):
                    if visit_A[i][0] > visit_A[i - 1][0]:

                        visit_A[i], visit_A[i - 1] = visit_A[i - 1], visit_A[i]
            if len(visit_B) >= 2:
                for i in range(len(visit_B) - 1, 0, -1):
                    if visit_B[i][0] > visit_B[i - 1][0]:
                        visit_B[i], visit_B[i - 1] = visit_B[i - 1], visit_B[i]

        if visit_A[0][1] == visit_B[0][1]:
            if len(visit_A) > 2 and len(visit_B) > 2:
                if visit_A[1][0] > visit_B[1][0]:
                    result += (visit_A[1][0] + visit_B[0][0])
                else:
                    result += (visit_A[0][0] + visit_B[1][0])
            elif len(visit_A) > 2:
                result += (visit_A[1][0] + visit_B[0][0])
            elif len(visit_B) > 2:
                result += (visit_A[0][0] + visit_B[1][0])
            else:
                result += visit_A[0][0]
        else:
            result += (visit_A[0][0] + visit_B[0][0])

        # 시간 1 증가
        time += 1


    print('#%d' %t, result)
