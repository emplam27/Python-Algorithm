import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

N, K = map(int, read().rstrip().split())
candidate_chars = dict()
already_in = set()
for _ in range(N):
    word = sorted(list(set(list(read().rstrip())) - {'a', 'n', 't', 'c', 'i'}))

    if candidate_chars.get(word):
        candidate_chars[word][0] += 1
    else:
        candidate_chars[word] = [1, 0]
print(candidate_chars)