import sys

sys.stdin = open("input.txt", "r")

'''
1시간 40분
결과값이 0일때인 케이스를 안잡아서 30분,  

<해야할 일>
1. N*H 배열에 가로선만을 표시, 조합을 이용해서 빈 자리에 1개부터 다리를 놓는다. 
2. 한칸씩 내려가면서 좌우에 가로선이 있는지 확인. 있다면 이동, 없으면 다음칸으로 내려감
3. 처음 출발지를 기억해 놓고 있다가 모두 시작점과 같게 나오면 종료, 아니면 다음경우의 수 탐색

<주의할 점>
1. 좌표 선택에 주의할 것. 사다리가 어떻게 놓여있는지 잘 봐야 함
'''

# def print_ladders():
#     for ladder in ladders:
#         print(*ladder)


from itertools import combinations


def check(results):
    # ladders에 가로선을 표시
    for r, c in results:
        ladders[r][c] = 1

    # 처음 세로선부터 시작하여 자기자신에 도착하는지 확인한다.
    for start in range(N):
        current, level = start, 0

        # 모든 층을 다 내려갔을 때, 처음이랑 똑같다면 continue, 아니라면 break
        while level < H:
            # 좌측으로 이동이 가능하다면
            if 0 <= current - 1 < N and ladders[level][current - 1] == 1:
                current, level = current - 1, level + 1

            # 우측으로 이동이 가능하다면
            elif 0 <= current + 1 < N and ladders[level][current] == 1:
                current, level = current + 1, level + 1

            # 좌우로 이동할 수 없다면
            else:
                level += 1

        # 하나라도 처음과 끝이 다르다면 종료
        if current != start:
            break

    else:  # 모두 같다면 True 반환
        return True

    # ladders를 원래대로 되돌린다.
    for r, c in results:
        ladders[r][c] = 0
    return False


N, M, H = map(int, input().split())
lines = [list(map(int, input().split())) for _ in range(M)]

if M == 0:
    print(0)
else:
    ladders = [[0] * N for _ in range(H)]
    for a, b in lines:
        ladders[a - 1][b - 1] = 1

    candidate = []  # 비어있는 곳 리스트
    for i in range(H):
        for j in range(N):
            # 두 가로선은 연속하면 안된다.
            if ladders[i][j] == 0:
                if 0 < j < N - 1:
                    if ladders[i][j - 1] == 0 and ladders[i][j + 1] == 0:
                        candidate.append([i, j])
                elif j == 0:
                    if ladders[i][j + 1] == 0:
                        candidate.append([i, j])
                else:
                    if ladders[i][j - 1] == 0:
                        candidate.append([i, j])

    # 빈곳들 중 조합을 이용해서 0, 1, 2, 3개 선정,
    for i in range(4):
        if i > len(candidate):
            print(-1)
            exit()
        comb_list = list(map(list, combinations(candidate, i)))
        for comb in comb_list:
            if check(comb):
                print(i)
                exit()
    print(-1)
