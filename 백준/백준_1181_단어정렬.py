import sys

sys.stdin = open('input.txt', 'r')

N = int(input())
words_by_len = [set() for _ in range(51)]
for _ in range(N):
    word = input()
    words_by_len[len(word)].add(word)
for words in words_by_len:
    if words:
        for word in sorted(words):
            print(word)
