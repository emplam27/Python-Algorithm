'''

<2개짜리 탑을 끝에 만들기>
1개짜리 탑을 중간에 만들기 => 두번째 판을 끝으로 옮기기 => 1개짜리 탑을 끝에 만들기

<3개짜리 탑을 끝에 만들기>
2개짜리 탑을 중간에 만들기 => 세번째 판을 끝으로 옮기기 => 2개짜리 탑을 끝에 만들기
다시쓰면
(1개짜리 탑을 끝에 만들기 => 두번째 판을 중간으로 옮기기 => 1개짜리 탑을 중간에 만들기)
=> 세번째 판을 끝으로 옮기기
=> (1개짜리 탑을 처음에 만들기 => 두번째 판을 끝으로 옮기기 => 1개짜리 탑을 끝에 만들기)

<4개짜리 탑을 끝에 만들기>
3개짜리 탑을 중간에 만들기 => 네번째 판을 끝으로 옮기기 => 3개짜리 탑을 끝에 만들기
다시쓰면
(2개짜리 탑을 끝에 만들기 => 세번째 판을 중간으로 옮기기 => 2개짜리 탑을 중간에 만들기)
=> 네번째 판을 끝으로 옮기기
=> (2개짜리 탑을 처음에 만들기 => 세번째 판을 끝으로 옮기기 => 2개짜리 탑을 끝에 만들기)

위 규칙을 참고하면
재귀함수에 필요한 인자: 층수, 시작점, 끝점
'''


import sys

sys.stdin = open('input.txt', 'r')


def make_hanoi_tower(floor, start_stage, end_stage):
    if floor == 1:
        results.append([str(start_stage), str(end_stage)])
        return

    mid_stage = 6 - (start_stage + end_stage)
    make_hanoi_tower(floor - 1, start_stage, mid_stage)
    results.append([str(start_stage), str(end_stage)])
    make_hanoi_tower(floor - 1, mid_stage, end_stage)


N = int(input())
count, result_count = 1, 1
while count < N:
    count, result_count = count + 1, 2 * result_count + 1
print(result_count)

if N <= 20:
    results = []
    make_hanoi_tower(N, 1, 3)
    for result in results:
        print(' '.join(result))


