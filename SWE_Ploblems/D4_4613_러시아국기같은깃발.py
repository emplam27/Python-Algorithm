"""
완전탐색 문제
각 색마다 줄수를 결정해서 모두 탐색하기

"""

import sys

sys.stdin = open("input.txt", "r")


def check_lines(start, end, color):

    unmatched = 0
    for i in range(end):
        for j in range(M):
            if flag[start + i][j] != color:
                unmatched += 1
    return unmatched


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]

    # 흰줄, 파란줄, 빨간줄 수 결정하기
    min_result = N * M
    for white_line in range(1, N - 1):
        for blue_line in range(1, N - white_line):
            red_line = N - (white_line + blue_line)

            # 결정된 패턴에 맞지않은 칸 수 세기
            tmp_result = (check_lines(0, white_line, 'W') + check_lines(white_line, blue_line, 'B') + check_lines(
                white_line+ blue_line, red_line, 'R'))
            if min_result > tmp_result:
                min_result = tmp_result

    print('#{} {}'.format(t, min_result))
