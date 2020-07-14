"""
dict를 이용해서 해보자.
combination을 이용해서 컬럼을 선정한 후, (column1, column2, ...)를 key로 하여 탐색한다.
defaultdict를 사용하여 없을경우 바로 value에 0을 넣어준다.
혹시나 key가 존재한다면 종료한다.
"""
from itertools import combinations


def solution(relations):
    answer = 0
    used_list = []
    nums = [i for i in range(len(relations[0]))]
    for i in range(1, len(nums) + 1):
        combi_list = list(combinations(nums, i))

        for combi_elem in combi_list:

            # 최소성 만족여부 확인
            is_unique = True
            for used in used_list:
                selected = 0
                for j in used:
                    if j in combi_elem:
                        selected += 1
                        continue
                if selected == len(used):  # 최소성을 벗어나면
                    is_unique = False
                    break
            if is_unique:
                # relation의 combi_elem 컬럼을 추가하며 검사
                check_key = dict()
                for relation in relations:
                    tmp_dict = []
                    for i in combi_elem:
                        tmp_dict.append(relation[i])
                    tmp_dict = tuple(tmp_dict)

                    if not check_key.get(tmp_dict):
                        check_key[tmp_dict] = 1
                    else:
                        break
                else:
                    answer += 1
                    used_list.append(combi_elem)

    return answer
