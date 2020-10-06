def solution(s):
    result = []

    # 1부터 절반까지만 구하기
    if len(s) == 1:
        return 1

    for crop_length in range(1, len(s) // 2 + 1):
        croped_string = []
        for idx in range(len(s) // crop_length):
            croped_string.append(s[crop_length * idx: crop_length * (idx + 1)])
        if len(s) % crop_length:
            croped_string.append(s[-(len(s) % crop_length):])

        current_result = ''
        current_srting, count = 0, 1
        for string_index in range(1, len(croped_string)):
            if croped_string[current_srting] == croped_string[string_index]:
                count += 1
            if croped_string[current_srting] != croped_string[string_index]:
                if count != 1:
                    current_result += (str(count) + croped_string[current_srting])
                else:
                    current_result += croped_string[current_srting]
                current_srting = string_index
                count = 1
        if count != 1:
            current_result += (str(count) + croped_string[current_srting])
        else:
            current_result += croped_string[current_srting]

        result.append(len(current_result))
    return min(result)