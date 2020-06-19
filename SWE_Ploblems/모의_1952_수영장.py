import sys

sys.stdin = open("input.txt", "r")


def check(idx, fee, visited):
    global min_fee
    if idx == 12:
        if fee < min_fee:
            min_fee = fee
        return

    if arr[idx] != 0 and visited[idx] == 0:
        # 하루권 사용시, arr
        fee += arr[idx] * d
        visited[idx] = 1
        check(idx + 1, fee, visited)
        fee -= arr[idx] * d
        visited[idx] = 0

        # 1개월권 사용시
        fee += m
        visited[idx] = 1
        check(idx + 1, fee, visited)
        fee -= m
        visited[idx] = 0

        # 3개월권 사용시
        fee += tm
        for i in range(3):
            if idx + i < 12:
                visited[idx + i] = 1
        check(idx + 1, fee, visited)
        for i in range(3):
            if idx + i < 12:
                visited[idx + i] = 0

    else:
        visited[idx] = 1
        check(idx + 1, fee, visited)
        visited[idx] = 0


T = int(input())
for t in range(1, T + 1):
    d, m, tm, y = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = [0] * 12
    min_fee = y

    check(0, 0, visited)

    print('#{} {}'.format(t, min_fee))

    # 부르투 포스를 이용하여 매월을 1일권 적용, 1개월권 적용, 3개월권 적용(비짓3개개)으로 모든경우의수 구기
    # 일일, 월, 3개월 사용권을 모두 적용한 뒤, 1년권이랑 비교한다.