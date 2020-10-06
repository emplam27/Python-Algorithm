def solution(words):
    answer = 0

    # 다차원 dict로 정리
    words_dict = dict()
    for word in words:
        current_dict = words_dict
        for char in word:
            if not current_dict.get(char):
                current_dict[char] = [1, dict()]
            else:
                current_dict[char][0] += 1
            current_dict = current_dict[char][1]

    # 검사
    for word in words:
        current_dict = words_dict
        for index, char in enumerate(word):
            if current_dict[char][0] != 1:
                current_dict = current_dict[char][1]
            else:
                answer += (index + 1)
                break
        else:
            answer += len(word)

    return answer

