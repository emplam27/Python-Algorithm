import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline


'''
<스택을 이용한 풀이>

스택에는 사각형들의 인덱스를 저장한다.

1. 스택의 마지막 인덱스 사각형의 높이보다 높은 사각형이 온다면, 해당 인덱스를 저장한다.
2. 아니라면 검사를 시작한다. 현재 사각형의 높이와 같은 높이가 나올 때 까지 pop 하면서 현재 인덱스를 기준으로 너비를 계산하며,
    너비와 높이를 곱해가며 사각형의 넓이를 구한다.
3. 최대 넓이를 갱신해주고, 다음 사각형으로 넘어가 넓이를 구한다.
'''


while True:
    N, *squares = list(map(int, read().rstrip().split()))
    if N == 0:
        break

    # 마지막 높이를 0으로 설정하여 모든 히스토그램에서 검사할 수 있도록 한다.
    squares.append(0)
    index_stack, max_result = [], 0
    for current_index, current_height in enumerate(squares):
        # 스택이 존재하고, 
        while index_stack and squares[index_stack[-1]] > current_height:
            last_index = index_stack.pop()
            width = ((current_index - 1) - index_stack[-1]) if index_stack else current_index
            square_area = squares[last_index] * width
            max_result = max(max_result, square_area)
        index_stack.append(current_index)
    print(max_result)
