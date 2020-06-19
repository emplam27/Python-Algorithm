import sys
sys.stdin = open("input.txt", "r")


# 한명의 사람이 갈 수 있는 계단은 2가지 경우의수 이므로, 조합을 구하여 어느계단으로 갈지 선택
def combination(idx, selected):
    global result

    if idx >= len(student):
        tmp1, tmp2, result1, result2, tmp_result = [], [], 0, 0, 0
        for i in range(len(student)):
            if selected[i] == 1:
                tmp1.append(abs(student[i][0] - stair[0][0]) + abs(student[i][1] - stair[0][1]))
            else:
                tmp2.append(abs(student[i][0] - stair[1][0]) + abs(student[i][1] - stair[1][1]))

        result1, result2 = check(tmp1, stair[0][2]), check(tmp2, stair[1][2])

        if result1 > result2:
            tmp_result = result1
        else:
            tmp_result = result2

        if result > tmp_result:
            result = tmp_result
        return

    selected[idx] = 0
    combination(idx + 1, selected)
    selected[idx] = 1
    combination(idx + 1, selected)


def check(tmp, duration):
    # ******************매우중요함*******************
    # 선택했다면, 그 계단으로 가는 최대 시간을 구함
    # 각각의 사람이 계단에 도착하는 시간을 구한 뒤, 배열로 만들어 정렬
    # 계단에 내려가고 있는 학생의 수를 구하는 counted 방문배열을 만든다
    # 학생이 도착하는 시간 이후로, 학생이 계단에 내려가고 있다면, 내려가는 동안을 += 1 하여 나타낸다
    # counted 배열의 요소가 3으로 차있다면, 이후 중 3이 아닌곳을 찾아 내려가기를 시작한다
    # 모든 학생들이 내려가게 되면, 배열을 역으로 순회하여 0이 아닌 요소가 처음으로 나오는 곳을 찾는다
    counted = [0] * 100
    tmp.sort()

    if len(tmp) == 0:
        return 0

    else:
        for l in tmp:
            while l < 100:
                l += 1
                if counted[l] < 3:
                    for m in range(l, l + duration):
                        counted[m] += 1
                    break

        for n in range(99, -1, -1):
            if counted[n] != 0:
                return n + 1


for t in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 사람, 계단의 위치를 아는 좌표를 만들기
    # 계단은 반드시 2개
    student, stair = [], []
    for i in range(N**2):
        if arr[i // N][i % N] == 1:
            student.append((i // N, i % N))
        elif arr[i // N][i % N] > 1:
            stair.append((i // N, i % N, arr[i // N][i % N]))

    # 조합
    result = 100000
    selected = [0] * len(student)
    combination(0, selected)

    print('#%d' %t, result)


