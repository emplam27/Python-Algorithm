def solution(board, moves):
    answer = 0

    # 인형 꺼내기. 0을 제외하고 가장 위쪽에 있는 숫자 고르기
    # stack에 인형 넣기. 만약 마지막 인형이 본인의 숫자와 같다면 마지막 숫자를 pop, answer += 2

    stack = []
    for move in moves:  # 가로
        for depth in range(len(board)):  # 세로
            if board[depth][move - 1] != 0:  # 제일 위 인형을 꺼낸다
                pick_doll, board[depth][move - 1] = board[depth][move - 1], 0
                break
        else:  # 빈 공간이었다면
            break  # 다음으로

        # 인형을 꺼냈을때 스택이 비어있으면 채워주고
        # 스택이 차있다면, 스택의 맨 위 인형과 비교
        if stack:
            if stack[-1] == pick_doll:
                stack.pop()
                answer += 2
            else:
                stack.append(pick_doll)
        else:
            stack.append(pick_doll)

    return answer