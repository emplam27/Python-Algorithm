import sys

sys.stdin = open("input.txt", "r")


# 요소갯수가 N개인 조합 함수
def combination(idx, cnt1, N, selected):

    if result != 0:
        return
    if cnt1 > N:
        return
    if idx >= D:
        if cnt1 == N:
            layer_list = list()
            for i in range(len(selected)):
                if selected[i] == 1:
                    layer_list.append(i)
                # 체크하는 함수 바로 실행
            injection(layer_list)
            if result != 0:
                return
        return

    selected[idx] = 0
    combination(idx + 1, cnt1, N, selected)
    selected[idx] = 1
    combination(idx + 1, cnt1 + 1, N, selected)


# 약품을 주입해서 배열을 변화시키는 함수
def injection(layer_list):
    global result
    # 배열복사
    copy_film = [[0] * W for _ in range(D)]
    for i in range(D):
        for j in range(W):
            copy_film[i][j] = film[i][j]

    # 약품 투입하여 A 또는 B로 만들기
    selected_layer = [0] * len(layer_list)
    injection_combi(0, layer_list, selected_layer, copy_film)


# 레이어를 조합하여 0, 1의 약품을 투입하는 함수
def injection_combi(layer_idx, layer_list, selected_layer, copy_film):
    global result
    if layer_idx >= len(layer_list):
        for r in range(len(layer_list)):
            if selected_layer[r] == 0:
                for s in range(W):
                    copy_film[layer_list[r]][s] = 0
            else:
                for s in range(W):
                    copy_film[layer_list[r]][s] = 1
        if check(copy_film):
            result = len(layer_list)
            return

        return

    selected_layer[layer_idx] = 0
    injection_combi(layer_idx + 1, layer_list, selected_layer, copy_film)
    selected_layer[layer_idx] = 1
    injection_combi(layer_idx + 1, layer_list, selected_layer, copy_film)


# 배열이 조건을 만족하는지 검사하는 함수
def check(copy_film):
    # 검사시작
    for p in range(W):
        tmp_int = copy_film[0][p]
        tmp_count, max_tmp_count = 1, 0
        for q in range(1, D):
            if tmp_int == copy_film[q][p]:
                tmp_count += 1
                if tmp_count >= K:
                    break
            else:
                tmp_int = copy_film[q][p]
                tmp_count = 1
        if tmp_count < K:
            break
            return
    else:
        return True


for t in range(1, int(input()) + 1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]

    # 0개일때 검사
    if check(film):
        print('#%d' % t, 0)

    else:
        # 0개보다 클때 검사
        result = 0
        for i in range(1, K):
            selected = [0] * D
            combination(0, 0, i, selected)
            if result != 0:
                print('#%d' % t, result)
                break

        else:
            print('#%d' % t, K)
