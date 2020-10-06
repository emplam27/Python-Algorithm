def solution(files):
    def make_list(file_name):
        head_index, number_index = 0, 0
        for index, value in enumerate(file_name):
            if value.isdecimal():
                head_index = index
                break

        for index in range(head_index, len(file_name)):
            if not file_name[index].isdecimal():
                number_index = index
                break
            if index > head_index + 4:
                number_index = index
                break
        else:
            return [file_name[: head_index], file_name[head_index: number_index], '']

        return [file_name[: head_index], file_name[head_index: number_index], file_name[number_index:]]

    # 데이터 가공 [HEAD, NUMBER, TAIL]
    for index, file in enumerate(files):
        files[index] = make_list(file)

    # HEAD가 같은 값끼리 묶기
    heads_list, heads_dict = list(), dict()
    for index, value in enumerate(files):
        head = value[0].lower()
        if not heads_dict.get(head):
            heads_dict[head] = [files[index]]
            heads_list.append(head)
        else:
            heads_dict[head].append(files[index])

    print(heads_dict)
    # 각 HEAD별 NUMBER로 정렬하기
    for key, value in heads_dict.items():
        value.sort(key=lambda x: int(x[1]))
        heads_dict[key] = value

    # HEAD 결과값 출력
    heads_list.sort()
    answer = []
    for key in heads_list:
        for value in heads_dict[key]:
            answer.append(''.join(value))

    return answer