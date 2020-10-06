"""
key를 90도씩 돌려서 완전탐색한다.

자물쇠의 홈과 열쇠의 돌기가 만나야만 함
각각의 홈끼리, 돌기끼리 만나면 안됨

자물쇠의 모든 홈을 채워야만 함
자물쇠의 홈 갯수를 찾고, 홈이 채워질 때 마다 -= 1씩 하자

"""


def solution(key, lock):
    def is_correct(key):

        # key의 왼쪽위를 기준으로 key가 움직일 수 있는 범위
        for key_r in range(-m + 1, n):
            for key_c in range(-m + 1, n):

                # key 중에서 lock과 겹치는 곳에서 검사
                success_count, check = lock_count, True
                for r in range(m):
                    for c in range(m):
                        nr, nc = key_r + r, key_c + c
                        if 0 <= nr < n and 0 <= nc < n:

                            # key 돌기와 lock 홈이 만나면 성공카운트 -= 1
                            if lock[nr][nc] == 0 and key[r][c] == 1:
                                success_count -= 1

                            # 돌기와 돌기가 만나거나 홈과 홈이 만나는 경우에는 다음 경우의수 탐색
                            elif lock[nr][nc] == key[r][c]:
                                check = False
                                break
                    if not check:
                        break
                if success_count == 0:
                    return True
        return False

    # lock의 홈 갯수 찾기
    m = len(key)
    n = len(lock)
    lock_count = 0
    for i in range(n ** 2):
        if lock[i // n][i % n] == 0:
            lock_count += 1

    for _ in range(4):
        if is_correct(key):
            return True
        key = list(map(list, zip(*key[::-1])))

    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
