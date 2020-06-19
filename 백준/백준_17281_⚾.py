# 1시간 30분
# 문제 꼼꼼히 읽을것
# 백준 제출은 시간초과남
# 해야할 일, 순서 잘 적어서 문제풀기
# 백준에 제출할때는 빠르게 해야하지만, 삼성은 직관성에 더 비중을 두도록 한다.


import sys

sys.stdin = open('input.txt', 'r')

# <해야할 일>

# 순열
# 완전탐색 문제이다. 순열을 만들어야 할 듯 하다.

# 야구게임
# 각 루를 배열로 나타내어 주고, 행동에 따라 그 배열을 변화시켜주는 방법으로 한다.
# 아웃이 3번 될때마다 필드를 초기화 하고 이닝을 1개 올린다.
# 3아웃이 되면 타자의 번호를 기억해 놓았다가 다음 이닝이 되면 그 다음 타자가 치게 된다.


# <순서>

# 1. 순열 만들어서 타자순서 정해주기, 야구함수 시작, 이미 실행한 경우에는 하지않기
# 2. 야구시작,


from itertools import permutations


def play_ball(order, N):
    global max_score

    # order에 4번타자 추가하기
    order = order[:3] + [0] + order[3:]

    # 게임을 시작하기위함 구성
    current_player = 0  # 현재 타자
    score = 0

    for inning in innings:

        # 반복문 시작
        base_1, base_2, base_3 = 0, 0, 0  # 1, 2, 3루에 사람이 있나 없나만 파악
        out_count = 0
        while out_count < 3:  # N 이닝을 넘어가면 종료
            if inning[order[current_player]] == 1:     # 1루타
                score += base_3
                base_1, base_2, base_3 = 1, base_1, base_2

            elif inning[order[current_player]] == 2:   # 2루타
                score += (base_2 + base_3)
                base_1, base_2, base_3 = 0, 1, base_1

            elif inning[order[current_player]] == 3:   # 3루타
                score += (base_1 + base_2 + base_3)
                base_1, base_2, base_3 = 0, 0, 1

            elif inning[order[current_player]] == 4:   # 홈런
                score += (1 + base_1 + base_2 + base_3)
                base_1, base_2, base_3 = 0, 0, 0

            else:  # 아웃
                out_count += 1

            # 타자순서가 끝났다면 0번부터 다시 친다.
            current_player += 1
            if current_player == 9:
                current_player = 0

    # 게임이 끝나면 점수를 갱신한다.
    if max_score < score:
        max_score = score
    return


N = int(sys.stdin.readline())
innings = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 순열 만들기
permutation = permutations(range(1, 9), 8)

# 순열을 순회하면서 게임
max_score = 0
for perm in permutation:
    play_ball(list(perm), N)

print(max_score)
