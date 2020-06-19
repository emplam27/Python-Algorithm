import sys

sys.stdin = open("input2.txt", "r")

# 54분

for testcase in range(1, int(input()) + 1):
    N, M, K, A, B = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t = list(map(int, input().split()))

    # 접수 창구의 개수 N, 정비 창구의 개수 M,
    # 차량 정비소를 방문한 고객의 수 K,
    # 지갑을 두고 간 고객이 이용한 접수 창구번호 A와 정비 창구번호 B
    # i번째 접수 창구가 고장을 접수하는 데 걸리는 시간 ai가 N개
    # j번째 정비 창구가 차량을 정비하는 데 걸리는 시간 bj가 M개
    # k번째 고객이 차량 정비소를 방문하는 시간 tk가 순서대로 K개

    # 고객이 가지고 있어야 할 정보: 본인 도착시간은 몇시인지, 몇번째 고객인지,
    # 접수는 몇번창구, 몇시간째, 정비는 몇번창구, 몇시간째
    for i in range(len(t)):
        t[i] = [t[i], i + 1, 0, 0, 0, 0]

    result_list, waiting_1, waiting_2 = [], [], []
    visit_a, visit_b = [0] * N, [0] * M
    time = 0
    while len(result_list) != K:

        # 도착한 사람 접수 대기열에 올려놓기
        for i in range(K):
            if t[i][0] == time:
                waiting_1.append(t[i])

        # 접수가 끝났다면 정비 대기열로 보내기.
        for i in range(N):
            if visit_a[i] != 0:
                if visit_a[i][3] == a[i]:
                    waiting_2.append(visit_a[i])
                    visit_a[i] = 0

        # 접수 대기열이 차있고, 접수창구가 비어있다면 접수창구로 보내기.
        for i in range(N):
            if visit_a[i] == 0 and len(waiting_1) > 0:
                waiting_1[0][2] = i + 1
                visit_a[i] = waiting_1.pop(0)

        # 정비가 끝났다면 결과값으로 보내기.
        for i in range(M):
            if visit_b[i] != 0:

                if visit_b[i][5] == b[i]:
                    result_list.append(visit_b[i])
                    visit_b[i] = 0

        # 정비 대기열이 차있고, 정비창구가 비어있다면 정비창구로 보내기.
        for i in range(M):
            if visit_b[i] == 0 and len(waiting_2) > 0:
                waiting_2[0][4] = i + 1
                visit_b[i] = waiting_2.pop(0)

        # 모든 창구 시간 1씩 증가시키기기
        for i in range(N):
            if visit_a[i] != 0:
                visit_a[i][3] += 1
        for i in range(M):
            if visit_b[i] != 0:
                visit_b[i][5] += 1
        time += 1

    result = 0
    for i in range(K):
        if result_list[i][2] == A and result_list[i][4] == B:
            result += result_list[i][1]
    if result == 0:
        result = -1
    # print(N, M, K, A, B, a, b)
    print('#%d' %testcase, result)
