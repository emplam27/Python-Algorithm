import sys

sys.stdin = open("input.txt", "r")

"""
50분 dict쓰면 더 빠를 것 같다.

<해야할 일>
1. 봄: 나무가 자신의 나이만큼 양분을 먹고 나이가 1 증가한다. 
    나이가 어린 나무부터 먹으며, 양분을 먹지 못하면 나무는 죽는다.
2. 여름: 죽은 나무마다 나이를 2로 나눈 값이 양분으로 추가된다.
    칸마다 봄을 처리한 후 여름을 처리하면 편할 것 같다.
3. 가을: 번식이 가능한 나무는 나이가 5의 배수이어야 하며, 인접한 8칸에 나이가 1인 나무를 만든다.
    같은칸에 여러 나무가 같이 있을 수 있으므로, 나무가 있더라도 번식이 가능하다.
4. 겨울: A배열과 동일하게 양분을 추가한다.

<주의할 점>
1. 나무 번식시에 같은 공간에 나무가 있더라도 상관이 없다.
2. 한공간에 여러 나무가 존재해야 하므로 배열을 한 요소를 양분의 양과 나무들로 구성하자
3. 나이가 어린 나무부터 양분을 먹기 때문에 정렬이 필요하다. 항상 작은나무는 앞쪽에다 집어넣는 것으로 하자.
"""

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
trees = [list(map(int, input().split())) for _ in range(M)]
field = [[[5, []] for _ in range(N)] for _ in range(N)]
dy, dx = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

# 나무 저장하기
for x, y, age in trees:
    if field[x - 1][y - 1][1]:
        field[x - 1][y - 1][1].append(age)
        field[x - 1][y - 1][1].sort()
    else:
        field[x - 1][y - 1][1].append(age)

# 시뮬레이션
for _ in range(K):

    # 봄, 여름 한번에 실행
    for r in range(N):  # 봄, 나이증가 및 죽음
        for c in range(N):
            if field[r][c][1]:  # 나무가 존재한다면
                for i, tree in enumerate(field[r][c][1]):  # 나무들을 순회하면서

                    dead_trees = []  # 죽은 나무들
                    # 앞 나무에서부터 양분을 먹여 나이를 늘린다.
                    if field[r][c][0] >= tree:
                        field[r][c][0] -= tree  # 양분줄이기
                        field[r][c][1][i] += 1  # 나이늘리기
                    # 양분을 먹지 못하면 dead_trees로 옮긴다.
                    else:
                        dead_trees = field[r][c][1][i:]
                        field[r][c][1] = field[r][c][1][:i]

                        # 여름, 죽은 나무 양분화
                        if dead_trees:
                            for dead_tree in dead_trees:
                                field[r][c][0] += dead_tree // 2
                        break

    # 가을, 나무 번식
    for r in range(N):
        for c in range(N):
            if field[r][c][1]:  # 나무가 존재한다면
                for i, tree in enumerate(field[r][c][1]):  # 나무들을 순회하면서
                    if field[r][c][1][i] % 5 == 0:  # 나이가 5의 배수이고
                        for d in range(8):
                            nr, nc = r + dy[d], c + dx[d]
                            if 0 <= nr < N and 0 <= nc < N:  # 범위안에 있이면
                                # 나이가 1인 나무 번식, 리스트의 제일 앞으로 넣어주기
                                field[nr][nc][1].insert(0, 1)

    # 겨울, 양분주기
    for r in range(N):
        for c in range(N):
            field[r][c][0] += A[r][c]

result = 0
for r in range(N):
    for c in range(N):
        result += len(field[r][c][1])
print(result)
