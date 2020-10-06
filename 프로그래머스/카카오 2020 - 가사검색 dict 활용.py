"""
words의 갯수를 trie 구조로 저장
접두사, 접미사의 두가지 케이스로 나누어 구분
{'count': 해당_문자_갯수, '문자': 문자별_하위_dict }로 구성
"""


def solution(words, queries):
    answer = []
    word_tries = [(dict(), dict()) for _ in range(10001)]

    # trie 구조 만들기
    for word in words:
        prefix_trie, suffix_trie = word_tries[len(word)]

        # 접두사 trie
        cur_prefix_dict = prefix_trie
        for char in word:
            cur_prefix_dict['count'] = cur_prefix_dict.get('count', 0) + 1
            if not cur_prefix_dict.get(char):
                cur_prefix_dict[char] = dict()
            cur_prefix_dict = cur_prefix_dict[char]

        # 접미사 trie
        cur_suffix_dict = suffix_trie
        for char in word[::-1]:
            cur_suffix_dict['count'] = cur_suffix_dict.get('count', 0) + 1
            if not cur_suffix_dict.get(char):
                cur_suffix_dict[char] = dict()
            cur_suffix_dict = cur_suffix_dict[char]

    # 가사 검색
    for query in queries:
        prefix_trie, suffix_trie = word_tries[len(query)]
        if query[0] != "?":  # 접두사
            current_dict = prefix_trie
        else:  # 접미사
            current_dict = suffix_trie
            query = query[::-1]
        result = current_dict.get('count', 0)  # word에 없는 길이의 query문이 등장할 수 있음

        for char in query:
            if char == "?":
                answer.append(result)
                break
            elif not current_dict.get(char):
                answer.append(0)
                break
            else:
                current_dict = current_dict[char]
                result = current_dict['count']

    return answer




