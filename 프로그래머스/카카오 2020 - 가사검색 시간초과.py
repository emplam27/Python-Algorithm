"""
길이가 같은 카드만 확인하도록 하기 위해서 길이별로 문자들을 모을 수 있는 배열을 만든다.
"""


def solution(words, queries):
    ordered_words = [[] for _ in range(100001)]
    for word in words:
        ordered_words[len(word)].append(word)

    result = []
    for query in queries:
        count = 0
        for word in ordered_words[len(query)]:
            for index, char in enumerate(word):
                if query[index] == '?':
                    continue
                else:
                    if query[index] == char:
                        continue
                    else:
                        break
            else:
                count += 1
        result.append(count)

    return result


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
