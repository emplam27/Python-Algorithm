def solution(words, queries):
    trie_by_length = [({}, {}) for _ in range(10001)]
    for word in words:
        length = len(word)
        t = trie_by_length[length][0]
        for c in word:
            t['count'] = t.get('count', 0) + 1
            t.setdefault(c, {})
            t = t[c]
        t = trie_by_length[length][1]
        for c in word[::-1]:
            t['count'] = t.get('count', 0) + 1
            t.setdefault(c, {})
            t = t[c]
    ans = []
    for query in queries:
        length = len(query)
        if query[0] == '?':
            t = trie_by_length[length][1]
            query = query[::-1]
        else:
            t = trie_by_length[length][0]
        for c in query:
            if c == '?':
                ans.append(t.get('count', 0))
                break
            if c not in t:
                ans.append(0)
                break
            t = t[c]
    return ans