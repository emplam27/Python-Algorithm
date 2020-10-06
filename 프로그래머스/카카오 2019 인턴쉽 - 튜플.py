def solution(s):
    s = s[1:-1].split('}')[:-1]
    for index, value in enumerate(s):
        s[index] = list(map(int, value.lstrip(',').lstrip('{').split(',')))

    tuple_dict = dict()
    for i in s:
        tuple_dict[len(i)] = i

    answer = []
    answer.append(tuple_dict[1][0])
    for i in range(2, len(tuple_dict) + 1):
        for j in tuple_dict[i]:
            if j not in answer:
                answer.append(j)

    return answer