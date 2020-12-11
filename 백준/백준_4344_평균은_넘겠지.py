import sys

sys.stdin = open('input.txt', 'r')

C = int(input())
for _ in range(C):
    tc = list(map(int, input().split()))
    N, scores = tc[0], tc[1:]
    score_avg = sum(scores) / len(scores)
    print(format(round(len(list(filter(lambda x: x > score_avg, scores))) / len(scores), 5) * 100, ".3f") + '%')

