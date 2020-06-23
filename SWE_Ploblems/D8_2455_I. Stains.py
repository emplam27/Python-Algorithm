import sys

sys.stdin = open("input.txt", "r")

''' 
백트레킹을 진행하는데, 얼룩이 있는 곳만 찾아서 재귀함수를 들어간다.
모든 얼룩을 지웠을 때, 사용한 도구의 갯수의 최솟값을 구한다.
'''


def cleaning(previous_n, previous_m, left_stain, result):
    global min_result

    if left_stain == 0:
        if min_result > result:
            min_result = result
        return

    # 이전에 청소한 칸의 줄부터 검사시작
    for n in range(previous_n, N - 1):
        for m in range(1, M - 1):

            # 만약 얼룩이 있다면
            for tmp_r, tmp_c in stains:
                if n <= tmp_r < n + 3 and m <= tmp_c < m + 3 and cleaned.get((tmp_r, tmp_c)) == 0:

                    # 청소하고 저장한 후 다음 재귀함수 호출
                    tmp_stains = []
                    for current_n in range(n, n + 3):
                        for current_m in range(m, m + 3):
                            if cleaned.get((current_n, current_m)) == 0:
                                cleaned[(current_n, current_m)] = 1
                                tmp_stains.append((current_n, current_m))

                    cleaning(n, m, left_stain - len(tmp_stains), result + 1)

                    # 다시 얼룩 표시
                    for stain_n, stain_m in tmp_stains:
                        cleaned[(stain_n, stain_m)] = 0


for t in range(1, int(input()) + 1):

    N, M = map(int, input().split())
    C = int(input())

    stains, cleaned = list(), dict() # 방문배열로 dict사용
    for _ in range(C):
        r, c = map(int, input().split())
        stains.append([r, c])
        cleaned[(r, c)] = 0

    min_result = float('inf')
    cleaning(1, 1, len(stains), 0)
    print('#{} {}'.format(t, min_result))
