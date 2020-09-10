"""
1. 보석의 모든 종류 수를 알아낸다.
2. 1부터 시작해서 보석 이름을 set에 집어넣고, len(set)의 길이가 같아지면 정지한다.
3. 멈춘 순간부터 위와 같은 방법이지만 반대방향로 다시 탐색한다.
4. 구해진 최소 범위를 저장하고, 그 다음부터 다시 구한다.
"""


def solution(gems):
    gems_num = len(set(gems))
    current_index, index = 0, 0
    results = []
    while index < len(gems):

        gems_set, index = set(), current_index
        while index < len(gems):
            gems_set.add(gems[index])
            # print(gems_set)
            if len(gems_set) == gems_num:
                end = index
                break
            index += 1
        else:
            break

        gems_set = set()
        while True:
            gems_set.add(gems[index])
            # print(gems_set)
            if len(gems_set) == gems_num:
                start = index
                current_index = index + 1
                break
            index -= 1

        results.append([start + 1, end + 1])

    # print(results)

    min_len = len(gems)
    result_index = 0
    for index, result in enumerate(results):
        if min_len > result[1] - result[0]:
            min_len = result[1] - result[0]
            result_index = index
    return results[result_index]