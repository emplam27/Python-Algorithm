# 도착하는 사람의 초가 에초애 만들 수 있는 숫자보다 작으면 무조건 불가능
# M초동안 K개 만드는데, 만약 M 부터 M +1 사이에 K명의 사람보다 적게 있다면 나눠주기 가능, 남은 붕어빵은 이월

import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N, M, K = map(int, input().split())
    # N 명 사람, M 초, K 개
    arr = list(map(int, input().split()))

    # M = 단위시간수
    # 누적된 사람수 변수 필요: N 이랑 같아지면 성공
    people = 0
    cnt = 0
    tmp_cnt = 0
    # # 쌓아놓은 붕어빵 수
    # bread += (K - M 타임에 먹은 사람수)
    bread = 0

    # 초기 실패조건 설정
    for j in range(N):
        if arr[j] < M:
            people = N + 1

    # 1명일때 성공조건
    if (N == 1) and (arr[0] > M):
        people = N

    # 사람수만큼 리스트에서 빼주고, 사람수가 0명이 되면 성공
    while people < N:
        for i in range(1, N):
            tmp_cnt = 0
            bread += K

            # 사람수 찾아내는법: 리스트를 돌면서 M 부터 M + 1 사이의 수를 리스트에서 찾자
            for k in range(N):
                if M * i <= arr[k] < M * (i+1):
                    tmp_cnt += 1

            # 누적된 bread + K < 사람수 라면 실패, 아니라면 성공
            if bread - tmp_cnt >= 0:
                # bread += (K - M 타임에 먹은 사람수)
                bread -= tmp_cnt
                people = people + tmp_cnt
            else:
                people = N + 1
                break

            if bread > N:
                people = N
                break

            if people == N:
                break

    if people == N:
        print('#%d' % t, 'Possible')
    else:
        print('#%d' % t, 'Impossible')
