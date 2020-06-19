import sys

sys.stdin = open("17135_input.txt", "r")

# 조합을 이용하여 성벽에 궁수 3명을 배치한다.
def combination(idx, count1, selected):

    if count1 > 3:
        return

    if idx >= M:
        if count1 == 3:
            tmp = []
            for i in range(len(selected)):
                if selected[i] == 1:
                    tmp.append(i)
            check(tmp)
        return

    selected[idx] = 1
    combination(idx + 1, count1 + 1, selected)
    selected[idx] = 0
    combination(idx + 1, count1, selected)


def check(arr):
    global max_result

    result = 0
    # field배열을 복사해서 사용
    field_copy = [([0] * M) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            field_copy[i][j] = field[i][j]

    count = 0
    while count < N:
        # arr의 한 요소씩 순화며, 거리가 가장 가까우며 왼쪽에 있는 적 찾기
        target = list()
        for k in arr:
            # 가장 번 줄부터 왼쪽에서 부터 순회하며 검사, 가장먼저 걸린 적을 저장, 거리가 가까워졌다면 갱신
            min_dis = 10000
            tmp_target = [0, 0]
            for i in range(N-D, N):
                for j in range(M):
                    if field_copy[i][j] == 1:
                        if abs(N-i) + abs(k-j) < min_dis:
                            min_dis = abs(N-i) + abs(k-j)
                            tmp_target = [i, j]
                        elif abs(N-i) + abs(k-j) == min_dis:
                            if tmp_target[1] > j:
                                tmp_target = [i, j]
            if (min_dis <= D) and (tmp_target not in target):
                target.append(tmp_target)

        result += len(target)
        if len(target) != 0:
            for i, j in target:
                field_copy[i][j] = 0

        for i in range(N-1, 0, -1):
            for j in range(M):
                field_copy[i][j] = field_copy[i-1][j]
        for i in range(M):
            field_copy[0][i] = 0
        count += 1

    if result > max_result:
        max_result = result

    return


N, M, D = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
selected = [0] * M

max_result = 0
combination(0, 0, selected)

print(max_result)

# first-line 이 사정거리보다 길면 그냥 전진
# 사정거리안에 들어온다면 탐색,
# 사정거리 안에 적이 3명 이하라면,


# 조합을 이용하여 성벽에 궁수 3명을 배치한다.
# 각 궁수들의 사정거리 안 적들중에서 가장 가까운 적을 선택한다. 내림차순으로 찾는다.
# 한턴에 최대로 잡을 수 있을만큼 배치하도록 한다.
# 성벽과 가까히 있는 적들은 우선적으로 잡도록 해야한다.
# 찾은 적들을 0으로 바꿔주고, 처치한 적의 수를 센 다음, 배열을 한줄씩 당긴다.
