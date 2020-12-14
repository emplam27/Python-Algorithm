def kmp(origin_text, compare_text):
    origin_cursor = 1  # 원본배열 커서
    compare_cursor = 0  # 비교배열 커서
    skip_table = [0] * (len(compare_text) + 1)  # 건너뛰기 표

    # 건너뛰기 표 만들기
    # skip_table[origin_cursor] = 0  # 왜?
    while origin_cursor != len(compare_text):

        # 건너뛰기 표
        if compare_text[origin_cursor] == compare_text[compare_cursor]:
            origin_cursor += 1
            compare_cursor += 1
            skip_table[origin_cursor] = compare_cursor
        elif compare_cursor == 0:
            origin_cursor += 1
            skip_table[origin_cursor] = compare_cursor
        else:
            compare_cursor = skip_table[compare_cursor]

    # 문자열 검색하기
    origin_cursor = compare_cursor = 0
    while origin_cursor != len(origin_text) and compare_cursor != len(compare_text):
        if origin_text[origin_cursor] == compare_text[compare_cursor]:
            origin_cursor += 1
            compare_cursor += 1
        elif compare_cursor == 0:
            origin_cursor += 1
        else:
            compare_cursor = skip_table[compare_cursor]

    return origin_cursor - compare_cursor if compare_cursor == len(compare_text) else -1


text_1 = 'AAAAAAAAAAAAAAAAAAAAAAA'
text_2 = 'AABCABDABB'

idx = kmp(text_1, text_2)

if idx == -1:
    print('x')
else:
    print(f'{idx + 1}')