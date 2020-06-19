# 50분
# 쪼개기가 필수다
# 좌표 문제는 웬만하면 배열로 해결하려 하자.

import sys

sys.stdin = open("2115_input.txt", "r")


def combi(idx, arr, tmp, tmp_selected):

    if idx >= len(arr):
        tmp_result, result = 0, 0
        for i in range(len(arr)):
            if tmp_selected[i] == 1:
                tmp_result += arr[i]
        if tmp_result > C:
            return
        else:
            for i in range(len(arr)):
                if tmp_selected[i] == 1:
                    result += arr[i]**2
            tmp.append(result)
        return

    tmp_selected[idx] = 1
    combi(idx + 1, arr, tmp, tmp_selected)
    tmp_selected[idx] = 0
    combi(idx + 1, arr, tmp, tmp_selected)


def check_result(arr):
    # 결과 구하는 함수
    # 배열을 순회하며, 선택시, 1로, 비선택시 0으로 하여 조합을 구하듯이 들어간다.
    # 배열마다 가장 큰 값을 저장했다가, 결과값을 갱신한다.
    tmp = []
    tmp_selected = [0] * len(arr)
    combi(0, arr, tmp, tmp_selected)
    return max(tmp)


# 벌통을 선택하는 완전 탐색 함수
def choice_comb(idx, selected, visited):
    # M번만큼 재귀를 들어간다. 한번 재귀를 들어갈 때 마다, 한명의 벌통을 선택하면서 들어간다.
    global max_result

    if idx >= 2:
        # 결과구하는 함수로 들어감
        result = 0
        for i in selected:
            result += check_result(i)
        if max_result < result:
            max_result = result
        return

    # 모든 배열을 순회하면서
    for r in range(N):
        for c in range(N):
            # 현위치 + M을 했을 시, 격자를 넘어가지 않으면서
            if c + (M-1) < N:
                # visited가 1인곳에 걸리지 않으면
                for m in range(M):
                    if visited[r][c + m] == 1:
                        break
                else:
                    # 괜찮은 위치
                    # 선택할 시, 새로운 배열에 선택한 꿀통의 배열을 저장하면서 들어간다. selected
                    for m in range(M):
                        visited[r][c + m] = 1
                        selected[idx].append(board[r][c + m])
                    choice_comb(idx + 1, selected, visited)
                    for m in range(M):
                        visited[r][c + m] = 0
                    selected[idx] = []


for t in range(1, int(input()) + 1):
    N, M, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    # N:벌통크기 N*N, M: 벌통선택갯수, C: 재쥐 최대양

    max_result = 0
    selected = [[] for _ in range(2)]
    visited = [[0] * N for _ in range(N)]
    choice_comb(0, selected, visited)

    print('#%d' %t, max_result)

