import sys

sys.stdin = open("input.txt", "r")


for t in range(1, 11):
    T = int(input())

    ladder = [list(map(int, input().split())) for _ in range(100)]
    idx_ladder = []
    for i in range(len(ladder)):
        tmp_arr = ladder[i].copy()
        idx_ladder.append(tmp_arr)

    min_cnt = 100000
    min_idx = 0

    for i in range(99, -1, -1):
        idx_ladder = []
        for idx in range(len(ladder)):
            tmp_arr = ladder[idx].copy()
            idx_ladder.append(tmp_arr)

        if idx_ladder[0][i] == 1:
            r = 0
            c = i
            cnt = 0
            while True:
                if r == 99:
                    break

                # 만일 c가 99라면 우측 못감
                if c == 99:
                    if idx_ladder[r][c - 1] == 1:
                        idx_ladder[r][c] = 0
                        c -= 1
                        cnt += 1
                        continue

                    if idx_ladder[r + 1][c] == 1:
                        idx_ladder[r][c] = 0
                        r += 1
                        cnt += 1
                        continue

                # 만일 c가 0라면 좌측 못감
                elif c == 0:
                    if idx_ladder[r][c + 1] == 1:
                        idx_ladder[r][c] = 0
                        c += 1
                        cnt += 1
                        continue

                    if idx_ladder[r + 1][c] == 1:
                        idx_ladder[r][c] = 0
                        r += 1
                        cnt += 1
                        continue

                else:
                    # 만일 좌측이 1이라면 좌방향으로 이동하는데, 0이 나오기 전까지 이동 혹은 좌표변경
                    if idx_ladder[r][c - 1] == 1:
                        idx_ladder[r][c] = 0
                        c -= 1
                        cnt += 1
                        continue

                    # 만일 우측이 1이라면 우방향으로 이동하는데, 0이 나오긴 전까지 이동 혹은 좌표변경
                    if idx_ladder[r][c + 1] == 1:
                        idx_ladder[r][c] = 0
                        c += 1
                        cnt += 1
                        continue

                    # 마지막으로 만일 하측만이 1이라면 아래로 1칸 이동
                    if idx_ladder[r + 1][c] == 1:
                        idx_ladder[r][c] = 0
                        r += 1
                        cnt += 1
                        continue

            if cnt < min_cnt:
                min_cnt = cnt
                min_idx = i

    print('#%d' %t, min_idx)
