def solution(stones, k):
    stones_dict = dict()
    for index, stone in enumerate(stones):
        if not stones_dict.get(stone):
            stones_dict[stone] = [index + 1]
        else:
            stones_dict[stone].append(index + 1)

    print(stones_dict)
    zero_list, result = [], 0
    while True:

        # 모든 원소의 값을 1 줄인 새로운 dict 구성하기
        current_dict = dict()
        for key, value in stones_dict.items():
            current_dict[key - 1] = value

        print(current_dict)
        # 0이 되는 원소들이 있다면 zero_list에 넣어주기
        if current_dict.get(0):
            zero_list.extend(current_dict[0])
            current_dict.pop(0)

        # zero_list를 정렬 후 검사하면서 연속된 k개의 수가 있는지 검사하기
        zero_list.sort()
        print(zero_list)
        for i in range(0, len(zero_list) - k):
            print(i, zero_list[i], sum(zero_list[i:i + k]), int((zero_list[i] + (k - 1) / 2) * k))
            if sum(zero_list[i:i + k]) == int((zero_list[i] + (k - 1) / 2) * k):
                break
        else:
            result += 1
            stones_dict = current_dict
            continue
        break

    return result

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
