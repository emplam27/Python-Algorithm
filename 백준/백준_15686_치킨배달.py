# import sys
#
# sys.stdin = open("15686_input.txt", "r")


# 남아있는 치킨집의 모든 경우의수를 찾는 함수
def power_set(selected, idx, count1):

    if idx == chic_cnt:
        if count1 == M:
            for i in range(chic_cnt):
                if selected[i] == 1:
                    remain_chic.append(chic_rest[i])

        return
    if count1 > M:
        return

    selected[idx] = 1
    count1 += 1
    power_set(selected, idx + 1, count1)
    count1 -= 1
    selected[idx] = 0
    power_set(selected, idx + 1, count1)


N, M = map(int, input().split())
village = [list(map(int, input().split())) for _ in range(N)]

# 집의 위치 리스트(house) 치킨집의 위치 리스트(chic_rest)와 갯수(chic_cnt) 가져오기
house = []
chic_rest = []
chic_cnt = 0
for i in range(N):
    for j in range(N):
        if village[i][j] == 2:
            chic_rest.append((i, j))
            chic_cnt += 1
        if village[i][j] == 1:
            house.append((i, j))


# 남아있는 치킨집 모든 경우의 수 구하기(closing_chic : cl_num 의 배수로 끊어서 읽어야함)
selected = [0] * chic_cnt
count1 = 0
remain_chic = []
# 모든 경우의 남아있는 치킨집을 찾는 함수실행
power_set(selected, 0, 0)


# 모든 집에서부터 가장 가까운 치킨집을 찾기
final_distance = 1000000000000
for i in range(len(remain_chic) // M):
    sum_distance = 0
    for r, c in house:
        min_distance = 10000000000000
        for j in range(M):
            distance = abs(r - remain_chic[M * i + j][0]) + abs(c - remain_chic[M * i + j][1])
            if distance < min_distance:
                min_distance = distance
        sum_distance += min_distance
    if sum_distance < final_distance:
        final_distance = sum_distance

print(final_distance)
