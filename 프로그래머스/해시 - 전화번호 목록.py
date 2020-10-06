def solution(phone_book):
    # trie 구조
    trie_dict = dict()
    for num in phone_book:
        cur_dict = trie_dict
        for index, value in enumerate(num):
            if not cur_dict.get(value):
                cur_dict[value] = dict()
            cur_dict = cur_dict[value]

    for num in phone_book:
        cur_dict = trie_dict
        for index, value in enumerate(num):
            if cur_dict.get(value):
                cur_dict = cur_dict[value]
            else:
                break
        else:
            return False
    return True