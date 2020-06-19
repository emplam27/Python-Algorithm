import sys

# 표준 입/출력 : 콘솔입출력
sys.stdin = open("input.txt", "r")  # 파일입력

T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    score = dict()
    score_list = list()

    for idx, a in enumerate(arr):
        score[idx + 1] = (0.35 * a[0] + 0.45 * a[1] + 0.2 * a[2])
        score_list.append(0.35 * a[0] + 0.45 * a[1] + 0.2 * a[2])

    score_list.sort()
    score_list.reverse()


    for i, j in enumerate(score_list):
        if score[K] == j:
            if i < 0.1 * N:
                print('#%d' %t, 'A+')
            if 0.1 * N <= i < 0.2 * N:
                print('#%d' % t, 'A0')
            if 0.2 * N <= i < 0.3 * N:
                print('#%d' % t, 'A-')
            if 0.3 * N <= i < 0.4 * N:
                print('#%d' % t, 'B+')
            if 0.4 * N <= i < 0.5 * N:
                print('#%d' % t, 'B0')
            if 0.5 * N <= i < 0.6 * N:
                print('#%d' % t, 'B-')
            if 0.6 * N <= i < 0.7 * N:
                print('#%d' % t, 'C+')
            if 0.7 * N <= i < 0.8 * N:
                print('#%d' % t, 'C0')
            if 0.8 * N <= i < 0.9 * N:
                print('#%d' % t, 'C-')
            if 0.9 * N <= i:
                print('#%d' % t, 'D0')




