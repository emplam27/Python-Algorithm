"""
2중 for문을 사용하지 않아야 시간복잡도가 줄어든다.
lambda sorted가 필요하다.
"""

def solution(N, stages):
    answer = []
    # [도달했으나 클리어 못한사람 수, 도달한 사람 수]
    fail_rate = [[0, 0] for i in range(N)]

    for stage in stages:
        # 도달하였고, 클리어도 하였음
        for i in range(stage - 1):
            fail_rate[i][1] += 1

        if stage != N + 1:
            # 도달하였으나 클리어하지 못하였음
            fail_rate[stage - 1][0] += 1
            fail_rate[stage - 1][1] += 1

    # [실패율 , index]로 정리하기
    for idx in range(len(fail_rate)):
        # 도달한 사람이 없으면 실패율은 0
        if fail_rate[idx][1] == 0:
            tmp_rate = 0
        else:
            tmp_rate = fail_rate[idx][0] / fail_rate[idx][1]
        fail_rate[idx] = [tmp_rate, idx + 1]

    # 실패율이 큰 순서부터 정리하기
    for _ in range(N):
        max_rate, max_index = -1, 0
        for i in range(len(fail_rate)):
            if max_rate < fail_rate[i][0]:
                max_rate = fail_rate[i][0]
                max_index = i
        answer.append(fail_rate[max_index][1])
        fail_rate.pop(max_index)

    return answer