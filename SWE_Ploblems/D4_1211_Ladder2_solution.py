import sys

sys.stdin = open("input.txt", "r")


for t in range(1, 11):
    T = int(input())

    ladder = [list(map(int, input().split())) for _ in range(100)]

    min_cnt = 10000
    min_idx = 0

    for i in range(100):
        if ladder[0][i] == 1:
            r = 1
            c = i
            cnt = 1
            direct = 1      # 1: 하, 2: 우, 3: 좌

            # 진행방향을 확인하고, 다음 갈 곳을 정의, 맨 마지막줄에 도착할 때 까지
            while r < 100:
                # 이동조건
                if direct == 1:     # 하방향
                    # 우방향 확인
                    if c + 1 < 100 and ladder[r][c + 1] == 1:
                        direct = 2  # 방향을 우방향으로 전환해주고
                        c += 1      # 우방향으로 이동

                    # 좌방향 확인
                    elif c - 1 > 0 and ladder[r][c - 1] == 1:
                        direct = 3  # 방향을 우방향으로 전환해주고
                        c -= 1      # 우방향으로 이동

                    # 좌, 우 방향 중 갈곳이 있으면 방향 전환
                    else:
                        r += 1  # 하방향으로 이동, direct 는 그대로.

                elif direct == 2:   # 우방향
                    # 하방향 확인
                    if ladder[r + 1][c] == 1:
                        direct = 1
                        r += 1
                    # 하방향으로 갈곳이 없으면 그대로 우방향 진행
                    else:
                        c += 1

                elif direct == 3:   # 좌방향
                    # 하방향 확인
                    if ladder[r + 1][c] == 1:
                        direct = 1
                        r += 1
                    # 하방향으로 갈곳이 없으면 그대로 좌방향 진행
                    else:
                        c -= 1
                cnt += 1

                if cnt > min_cnt:   # 제일 짧은 경로만 필요하기 때문에 큰 cnt 는 필요없다.
                    break

            if cnt <= min_cnt:
                min_cnt = cnt
                min_idx = i

    print('#%d' % t, min_idx)
