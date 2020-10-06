"""
길이가 같은 카드만 확인하도록 하기 위해서 길이별로 문자들을 모을 수 있는 배열을 만든다.

<아이디어>
문자열의 정렬을 이용한다. 문자열을 정렬하게 되면 알파벳 순서대로 정렬이 수행된다.
따라서 2진 탐색을 이용, 해당 query가 성립하기 시작하는 인덱스, 끝나는 인덱스를 찾아 빼주어 갯수를 구할 수 있다.
?가 접미사일 경우에는, 모든 word를 반대로 뒤집어 정렬하여 같은 방법으로 해결할 수 있다.
"""


def check_query(query, words_arr):
    # 성립하기 시작하는 인덱스 찾기
    start, end = 0, len(words_arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if words_arr[mid] < query:  # query가 더 크면
            start = mid + 1
        else:  # query가 더 작으면
            end = mid - 1
    start_index = start

    # 성립이 끝나는 인덱스 찾기
    # ?를 빼준 후, word를 같은 길이로 만들어 비교
    query = query.rstrip('?')
    l = len(query)
    end = len(words_arr) - 1  # start 그대로 사용
    while start <= end:
        mid = (start + end) // 2
        if words_arr[mid][:l] == query:
            start = mid + 1
        else:
            end = mid - 1
    end_index = start

    return end_index - start_index


def solution(words, queries):
    ordered_words = [[] for _ in range(100001)]
    ordered_rev_words = [[] for _ in range(100001)]

    # 길이에 해당하는 인덱스에 추가해주기
    for word in words:
        ordered_words[len(word)].append(word)
        ordered_rev_words[len(word)].append(word[::-1])

    # 각 길이별로 정렬 수행
    for i in range(100001):
        ordered_words[i].sort()
        ordered_rev_words[i].sort()

    # query를 순회하면서 이진탐색을 이용해서 찾기
    result = [0] * len(queries)
    for index, query in enumerate(queries):
        if query[0] != '?':
            result[index] = check_query(query, ordered_words[len(query)])
        else:
            result[index] = check_query(query[::-1], ordered_rev_words[len(query)])

    return result
