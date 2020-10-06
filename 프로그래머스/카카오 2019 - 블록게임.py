"""
각 블럭마다 검은블록으로 채워질 수 있는 후보 칸들이 존재한다.
그 후보칸들의 윗 방향에 아무것도 없다면, 없앨 수 있는 블럭이다. 하나라도 있다면 없앨 수 없는  블럭이다.
한번의 블럭을 없애고 나면 다시 검사하고, 모두 검사했을 때 없앨 블럭이 없다면 종료한다.

후보칸은 칸들 중 위, 아래, 좌, 우에서 가장 큰 값들을 이용하여 찾자.
"""


def solution(board):
    N = len(board)
    blocks = [[] for _ in range(201)]  # 기존 블럭들의 배열
    candidate_blocks = [[] for _ in range(201)]  # 검은블럭이 들어갈 후보칸들의 배열
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                blocks[board[i][j]].append([i, j])

    # 검은블럭 후보자리 찾기
    for index, block in enumerate(blocks):
        if block:
            top, bottom, left, right = block[0][0], block[0][0], block[0][1], block[0][1]
            for b in block:
                if b[0] < top:
                    top = b[0]
                elif b[0] > bottom:
                    bottom = b[0]
                if b[1] < left:
                    left = b[1]
                elif b[1] > right:
                    right = b[1]

            # 6칸 중에서 b안에 포함되지 않은 칸이 후보자리
            candidate = []
            for r in range(top, bottom + 1):
                for c in range(left, right + 1):
                    if [r, c] in block:
                        continue
                    else:
                        candidate.append([r, c])
            # 후보들 저장
            candidate_blocks[index] = candidate

    answer = 0
    while True:
        # 윗 방향 중 막혀있는 곳이 발견되면 다음 블럭으로 넘어간다.
        for index, candidate_block in enumerate(candidate_blocks):
            if candidate_block:
                for block in candidate_block:
                    r, c = block
                    while r >= 0:
                        if board[r][c] != 0:  # 위에 블럭이 있으면 종료
                            break
                        r -= 1
                    else:  # 블럭이 없으면 다음블럭 탐색
                        continue
                    break  # 블럭이 있으면 반복문 종료
                else:  # 두 후보 블럭의 위에 아무것도 없으면
                    answer += 1
                    for i, j in blocks[index]:  # 해당 블록을 없애주고
                        board[i][j] = 0
                    candidate_blocks[index] = []  # 후보도 없애준다.
                    break
        else:  # 모든 후보블럭의 위가 막혀있다면 while문을 종료한다.
            break
        continue  # 아니라면 while문을 다시 실행한다.

    return answer
