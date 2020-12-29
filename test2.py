import sys

sys.stdin = open("input.txt", "r")
read = sys.stdin.readline
M, N = map(int, read().rstrip().split())
stack = []
ocean = [list(map(int, read().rstrip().split())) for _ in range(M)]
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)


def melt(x, y):
    result = ocean[x][y]
    for i in range(4):
        temp_x = x + dx[i]
        temp_y = y + dy[i]
        if ocean[temp_x][temp_y] == 0:
            result -= 1
    if result <= 0:
        return 0
    else:
        return result


def dfs():
    answer = 0
    while True:
        glacier = 0
        temp_dic = dict()
        for x in range(1, M - 1):
            for y in range(1, N - 1):
                if ocean[x][y] and (x, y) not in temp_dic:
                    glacier += 1
                    stack.append((x, y))
                    temp_dic[(x, y)] = melt(x, y)
                    while stack:
                        x, y = stack.pop()
                        temp_dic[(x, y)] = melt(x, y)
                        for i in range(4):
                            temp_x = x + dx[i]
                            temp_y = y + dy[i]
                            if ocean[temp_x][temp_y] and (temp_x, temp_y) not in temp_dic:
                                stack.append((temp_x, temp_y))
        # print(temp_dic)
        if glacier == 0:
            return 0
        if glacier >= 2:
            return answer
        for key, value in temp_dic.items():
            x, y = key
            ocean[x][y] = value
        answer += 1
        # for i in range(M):
        #     print(*ocean[i])


print(dfs())
