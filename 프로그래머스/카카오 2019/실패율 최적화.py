def solution(N, stages):
    answer = []
    users = [0] * (N + 2)

    # 도달한 스테이지 배열 만들기
    for stage in stages:
        users[stage] += 1

    # 스테이지 클리어 유저 수 누적하기
    for stage in range(N, 0, -1):
        users[stage] += users[stage + 1]

    # [실패율, index]로 정리하기
    fail_rate = []
    for stage in range(1, N + 1):
        if users[stage] == 0:
            fail_rate.append([0, stage])
        else:
            fail_rate.append([1 - (users[stage + 1] / users[stage]), stage])

    # 정렬하기
    fail_rate.sort(key=lambda x: x[0], reverse=True)
    return [i[1] for i in fail_rate]
