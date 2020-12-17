import sys

sys.stdin = open('input.txt', 'r')

'''
먼저 볼의 갯수만큼 candidate를 임의로 정해서 넣어준다. 
candidate는 주어진 숫자 안에 그 숫자만큼 들어가 있는지 확인한다.


스트라이크가 1개 또는 2개인 경우에는 세 자리수 중 n를 선택해서 fixed에 정해놓는다.
스트라이크가 3개인 경우에는 result를 1개로 종료한다.


'''



# def play_game(index, fixed, cadidate):
#
#     if index == N:
#
#         return
#
#     check_num = list(str(question[index][0]))
#     strike = question[index][1]
#     ball = question[index][2]
#
#     if strike == 1:
#         for i in range(3):
#             if not fixed[i]:
#                 fixed[i] = check_num[i]
#                 play_game(index + 1, fixed)
#                 fixed[i] = None
#     elif strike == 2:
#         for i in range(3):
#             for j in range(i + 1, 3):
#                 if not fixed[i] and not fixed[j]:
#                     fixed[i], fixed[j] = check_num[i], check_num[j]
#                     play_game(index + 1, fixed)
#                     fixed[i], fixed[j] = None, None
#     elif strike == 3:
#         print(1)
#         exit()


def check(number, check_number, strike, ball):

    # 스트라이크 판별
    tmp_strike, strike_check = 0, []
    for i in range(3):
        if number[i] == check_number[i]:
            tmp_strike += 1
            strike_check.append(number[i])

    # 볼판별
    tmp_ball = 0
    for i in range(3):
        if number[i] not in strike_check and number[i] in check_number:
            tmp_ball += 1

    if strike == tmp_strike and ball == tmp_ball:
        return True


N = int(input())

question = [[list(str(val[0])), val[1], val[2]] for idx, val in enumerate([list(map(int, input().split())) for _ in range(N)])]
candidate, result = [], 0
for idx, val in enumerate(range(1000)):
    a, b, c = val // 100, (val % 100) // 10, val % 10
    if val > 100 and a > 0 and b > 0 and c > 0 and a != b and b != c and c != a:
        candidate.append(idx)

for _, val in enumerate(candidate):
    for index in range(N):
        if not check(list(str(val)), *question[index]):
            break
    else:
        result += 1
print(result)
