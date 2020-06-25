import sys

sys.stdin = open("input.txt", "r")

'''
<해야할 일>
1. 배열을 순회하면서 선정해보자.
2. 상하좌우로 섞여있어야 하기에 한줄로 이어지게 되는 DFS는 적합하지 않다.
3. 임의로 학생을 선택하여 이어져있는지를 확인하는 방법이 있다.

<주의할 점>
1. S들이 항상 4명 이상이여야 함. S와 Y의 수를 나타낼 수 있는 인자를 들고다녀야 함
2. 이미 완성된 경우의 수는 다시 정하면 안된다. 겹치는 경우의수를 어떤방법으로 처리할 것인가?
   
   한 특정 점에서 시작해서 list에 [{(지나온 지점들)}, S의 수, Y의 수]를 만들어서 붙이자.
   지나온 지점들 리스트를 순회하면서 사방으로 이동할 수 있도록 하자.
   가려고 하는 점이 지나온 지점들에 있으면 가지 않고, 이동할 수 있다면... 폐기
   
   배열을 이용해서 visited를 처리할 것인가? 처리한다면 7차원 배열을 이용해서 처리해볼까?
   visited배열의 경우에는 번호를 매겨서 할 것이냐, 상하좌우를 사용해서 할 것이냐?
   visited = [[[[[[[0] * 25 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(25)]
   번호는 25개의 공간, 상하좌우는 4개의 공간만 필요하니 상하좌우로 해보자... 폐기
   
   인접한 학생들을 찾아가면서 문제를 해결하는 방식은 너무 문제가 많다. visited를 활용하기에 만만치 않다.
   임의의 학생들을 골라 이어져있는지 확인하는 방법이 더 나을 듯 하다. 조합을 만들어서 해결하자.
   조합을 만드는 과정에서 Y가 세명을 넘어가는지 확인하면 될 듯 하다.
   이어져있는 친구들은 어떤식으로 찾을것인가? 이때 DFS 사용
'''


def combination(index, selected, count_girl, count_y):
    global result

    if count_y > 3:
        return

    if count_girl >= 7:
        # selected 가공하기
        candidate = []
        for i in range(25):
            if selected[i]:
                candidate.append([i // 5, i % 5])
        if is_connected(candidate):
            result += 1
        return

    if index >= 25:
        return

    selected[index] = 1
    if classroom[index // 5][index % 5] == 'Y':  # Y이면
        combination(index + 1, selected, count_girl + 1, count_y + 1,)
    else:
        combination(index + 1, selected, count_girl + 1, count_y)
    selected[index] = 0
    combination(index + 1, selected, count_girl, count_y)


def is_connected(arr):
    visited = [0] * 7
    stack = [arr[0]]
    visited[0] = 1
    connect_count = 1

    while stack:
        r, c = stack.pop()
        for d in range(4):
            nr, nc = r + dy[d], c + dx[d]
            if [nr, nc] in arr and not visited[arr.index([nr, nc])]:
                visited[arr.index([nr, nc])] = 1
                stack.append([nr, nc])
                connect_count += 1

    if connect_count == 7:
        return True
    else:
        return False


classroom = [list(input()) for _ in range(5)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

result, selected = 0, [0] * 25
combination(0, selected, 0, 0)
print(result)
