# 해당 문제는 큰것부터 집어넣는것이 정답이 아님. 
# 각 넣을 수 있는 곳에서 큰것부터 차례로 넣어줘야 함. greedy가 아닌 bruteforce문제


# for문을 여러개 작성하게되면 디버깅 시에 매우 복잡해진다.
# 함수를 잘게 쪼개어 사용하는게 문제 풀기에는 훨씬 좋다.


import sys

sys.stdin = open("17136_input.txt", "r")


def result_check():
    # board에 1이 없으면  True, 있으면 False를 리턴
    for i in range(100):
        if board[i//10][i%10] == 1:
            return False
    return True


def size_available(size, r, c):
    for nr in range(r, r + size + 1):
        for nc in range(c, c + size + 1):
            if nr >= 10 or nc >= 10 or board[nr][nc] == 0:
                return False
    return True


def change_0(size, r, c):
    for nr in range(r, r + size + 1):
        for nc in range(c, c + size + 1):
            board[nr][nc] = 0


def change_1(size, r, c):
    for nr in range(r, r + size + 1):
        for nc in range(c, c + size + 1):
            board[nr][nc] = 1


def check(visited, result):
    global min_result

    # board에 1이 없으면 result를 갱신한다.
    tmp_result = result_check()
    if tmp_result:
        if min_result > result:
            min_result = result
        return

    # visited가 모두 차있으면 return한다.
    for j in range(5):
        if visited[j] < 5:
            break
    else:
        return

    # visited가 안차있으면, 그 색종이를 빈자리에 붙이러 간다.
    for i in range(100):
        if board[i // 10][i % 10] == 1:
            for size in range(5):
                if size_available(size, i//10, i%10) == True and visited[size] < 5:
                    change_0(size, i//10, i%10)
                    visited[size] += 1
                    check(visited, result + 1)
                    change_1(size, i//10, i%10)
                    visited[size] -= 1
            break


board = [list(map(int, input().split())) for _ in range(10)]
visited = [0] * 5
min_result = 25
check(visited, 0)
if min_result == 25:
    min_result = -1
print(min_result)