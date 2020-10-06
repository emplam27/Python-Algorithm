"""
왼손, 오른손의 위치를 저장하는 배열을 생성

1. 1, 4, 7 인 경우에는 L을 이동 / 3, 6, 9인 경우에는 R을 이동
2. 2, 5, 8, 0 인 경우에는 거리를 계산하여 어느 손이 누를지 결정, 해당 손을 이동
3. 두 손 까지의 거리가 같다면 hand값으로 이동, 해당 손을 이동
4. 0인 경우도 생각해야 함.

[0, 0], [0, 1], [0, 2],
[1, 0], [1, 1], [1, 2],
[2, 0], [2, 1], [2, 2],
[3, 1]

[number // 3, number % 3 - 1]
"""


def solution(numbers, hand):
    # 왼손, 오른손 좌표
    hand_location = [[3, 0], [3, 2]]

    # 숫자별로 돌아가면서 손 위치 이동
    result = ''
    for number in numbers:

        # 숫자 위치 정하기
        if number == 3 or number == 6 or number == 9:
            number_location = [number // 3 - 1, 2]
        elif number != 0:
            number_location = [number // 3, number % 3 - 1]
        else:
            number_location = [3, 1]

        # 1, 4, 7
        if number == 1 or number == 4 or number == 7:
            hand_location[0] = number_location
            result += 'L'

        # 3, 6, 9
        elif number == 3 or number == 6 or number == 9:
            hand_location[1] = number_location
            result += 'R'

        # 2, 5, 8, 0
        else:

            left_dictance = abs(hand_location[0][0] - number_location[0]) + abs(
                hand_location[0][1] - number_location[1])
            right_distance = abs(hand_location[1][0] - number_location[0]) + abs(
                hand_location[1][1] - number_location[1])
            # 왼손이 더 가까우면
            if left_dictance < right_distance:
                hand_location[0] = number_location
                result += 'L'

            # 오른손이 더 가까우면
            elif left_dictance > right_distance:
                hand_location[1] = number_location
                result += 'R'

            # 거리가 같다면
            else:
                # 왼손잡이라면
                if hand == 'left':
                    hand_location[0] = number_location
                    result += 'L'

                # 오른손잡이라면
                else:
                    hand_location[1] = number_location
                    result += 'R'

    return result