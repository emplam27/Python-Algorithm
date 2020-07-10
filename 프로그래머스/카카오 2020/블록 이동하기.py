"""
상하좌우 이동 및 90도 회전을 위한 리스트가 필요함.
로봇이 가로 방향일 때, 세로 방향일 때, 시계방향일 때, 반시계 방향일 때 회전의 조건이 다르므로, 분기

항상 position은 [좌, 우] 또는 [상, 하]를 유지하게 한다.

이동배열의 인덱스 = [
로봇의 상우하좌 이동 [0]
로봇이 가로방향일 때 [1]
    오른쪽을 기준으로 [0]
        시계뱡항 90도 회전[0]
            왼쪽칸 우상방향 이동[0], 기준의 위쪽 블럭 검사 [1]
        반시계뱡항 90도 회전[1]
            왼쪽칸 우하방향 이동[0], 기준의 아래쪽 블럭 검사[1]
    왼쪽을 기준으로 [1]
        시계뱡항 90도 회전[0]
            오른쪽칸 좌하방향 이동[0], 기준의 아래쪽 블럭 검사[1]
        반시계뱡항 90도 회전[1]
            오른쪽칸 좌상방향 이동[0], 기준의 위쪽 블럭 검사[1]
로봇이 세로방향일 때 [2]
    위쪽을 기준으로 [0]
        시계뱡항 90도 회전[0]
            아래쪽칸 좌상방향 이동[0], 기준의 왼쪽 블럭 검사[1]
        반시계뱡항 90도 회전[1]
            아래쪽칸 우상방향 이동[0], 기준의 오른쪽 블럭 검사[1]
    아래쪽을 기준으로 [1]
        시계뱡항 90도 회전[0]
            위쪽칸 우하방향 이동[0], 기준의 오른쪽 블럭 검사[1]
        반시계뱡항 90도 회전[1]
            위쪽칸 좌하방향 이동[0], 기준의 왼쪽 블럭 검사[1]
]
"""


def solution(board):
    def move_robot(position, direction, result):
        nonlocal min_result

        # 최소경우보다 큰 탐색은 걸러주기
        if result > min_result:
            return

        # 도착하면 기록 갱신
        if [n, n] in position:
            if min_result > result:
                min_result = result
            return

        # 평행이동
        for d in range(4):
            change_position = [
                [position[0][0] + moves[0][0][d], position[0][1] + moves[0][1][d]],
                [position[1][0] + moves[0][0][d], position[1][1] + moves[0][1][d]],
            ]
            # 범위안에 존재하고
            if 0 <= change_position[0][0] < n and 0 <= change_position[0][1] < n \
                    and 0 <= change_position[1][0] < n and 0 <= change_position[1][1] < n \
                    and not board[change_position[0][0]][change_position[0][1]] \
                    and not board[change_position[1][0]][change_position[1][1]]:
                # 한칸이라도 방문하지 않았다면
                if not visited[change_position[0][0]][change_position[0][1]] \
                        or not visited[change_position[1][0]][change_position[1][1]]:
                    # 가로 방향일 때 상하 이동, 세로 방향일 때 좌우 이동
                    if (direction == 1 and d == (0 or 2)) or (direction == 2 and d == (1 or 3)):
                        visited[change_position[0][0]][change_position[0][1]] = 1
                        visited[change_position[1][0]][change_position[1][1]] = 1
                        move_robot(change_position, direction, result + 1)
                        visited[change_position[0][0]][change_position[0][1]] = 0
                        visited[change_position[1][0]][change_position[1][1]] = 0

                    # 가로 방향일 때 좌우 이동, 세로방향일 때 상하 이동
                    else:
                        if change_position[0] in position:
                            visited[change_position[1][0]][change_position[1][1]] = 1
                            move_robot(change_position, direction, result + 1)
                            visited[change_position[1][0]][change_position[1][1]] = 0

                        else:
                            visited[change_position[0][0]][change_position[0][1]] = 1
                            move_robot(change_position, direction, result + 1)
                            visited[change_position[0][0]][change_position[0][1]] = 0

        # 로봇의 방향에 따른 회전이동
        if direction == 1:
            direction = 2
        else:
            direction = 1

        for moving, pivot in enumerate([1, 0]):  # 기준점
            for rotate in [0, 1]:  # 시계방향, 반시계방향
                # 회전을 위해 비어있어야 할 블럭 검사
                check_point = [
                    position[moving][0] + moves[direction][pivot][rotate][1][0],
                    position[moving][1] + moves[direction][pivot][rotate][1][1]
                ]

                # 회전
                if 0 <= check_point[0] < n and 0 <= check_point[1] < n and not board[check_point[0]][check_point[1]]:
                    if pivot == rotate:
                        change_position = [check_point, position[1]]
                        visited[check_point[0]][check_point[1]] = 1
                        move_robot(change_position, direction, result + 1)
                        visited[check_point[0]][check_point[1]] = 0
                    else:
                        change_position = [position[0], check_point]
                        visited[check_point[0]][check_point[1]] = 1
                        move_robot(change_position, direction, result + 1)
                        visited[check_point[0]][check_point[1]] = 0

    n = len(board)
    visited = [[0] * n for _ in range(n)]
    visited[0][0], visited[0][1] = 1, 1
    moves = [
        [[-1, 0, 1, 0], [0, 1, 0, -1]],  # 상, 우, 하, 좌
        # 로봇 가로방향[왼쪽 기준[시계방향[이동하는 칸 이동경로, 기준칸 대비 검사 칸 위치], 반시계방향[...]], 오른쪽기준[...]]
        [[[[-1, -1], [-1, 0]], [[1, -1], [1, 0]]], [[[1, 1], [1, 0]], [[-1, 1], [-1, 0]]]],
        # 로봇 세로방향[위쪽 기준[시계방향[이동하는 칸 이동경로, 기준칸 대비 검사 칸 위치], 반시계방향[...]], 아레쪽기준[...]]
        [[[[-1, -1], [0, -1]], [[-1, 1], [0, 1]]], [[[1, 1], [0, 1]], [[1, -1], [0, -1]]]]
    ]

    min_result = n ** 2
    move_robot([[0, 0], [0, 1]], 1, 0)

    return min_result


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
