import sys
sys.stdin = open("input.txt", "r")

def check(arr):
    global result

    visited = [0] * N
    tmp = arr[0]
    for i in range(N):
        if arr[i] != tmp:
            # 높을 때
            if arr[i] > tmp and arr[i] - tmp == 1:
                for j in range(1, X + 1):
                    if 0 > i - j or i - j >= N:
                        return
                    if arr[i - j] != tmp:
                        return
                    if visited[i - j] != 0:
                        return
                # 성립시
                tmp = arr[i]
                for j in range(1, X + 1):
                    visited[i - j] = 1
                continue

            # 낮을 때
            elif arr[i] < tmp and tmp - arr[i] == 1:
                for j in range(1, X + 1):
                    if 0 > i - 1 + j or i - 1 + j >= N:
                        return
                    if arr[i - 1 + j] != tmp - 1:
                        return
                    if visited[i - 1 + j] != 0:
                        return
                # 성립시
                tmp = arr[i]
                for j in range(1, X + 1):
                    visited[i - 1 + j] = 1
                continue

            # 2이상 차이날 때
            else:
                return
    # 모두 성립시
    result += 1
    return


N, X = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
field_zip = list(map(list, zip(*field)))

# 무조건 안되는 경우
# 한번에 2씩 높아지는 경우
# 숫자가 변하는데, X 만큼의 여유가 없는경우
#

# 위로올라가는 활주로 놓기 : 현재값을 가지고 가다가, 자기보다 1 큰 값이 나오게 되면,
# 큰 값이 나온 기점으로 X번 후의 값들을 검사해서 다 같은 값이면 경사로 놓기 가능

# 아래로 내려가는 활주로 놓기 : 위랑 동일, 앞으로 X개를 확인하는 것

result = 0
for i in range(N):
    check(field[i])
    check(field_zip[i])

print(result)