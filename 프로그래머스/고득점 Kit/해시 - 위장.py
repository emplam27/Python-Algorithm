"""
1. 같은 종류의 물건끼리 dict로 묶기
2. 공집합을 제외한 집합을 구하면 됨. (2개, 1개) 라면 (2 + 1) * (1 + 1) - 1 의 값을 가짐
"""


def solution(clothes):
    clothe_dict = dict()
    for name, clothe in clothes:
        if not clothe_dict.get(clothe):
            clothe_dict[clothe] = 1
        else:
            clothe_dict[clothe] += 1

    result = 1
    for value in clothe_dict.values():
        result *= (value + 1)

    return result - 1