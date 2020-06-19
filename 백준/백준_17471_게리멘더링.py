import sys

sys.stdin = open("17471_input.txt", "r")


# 갯수가 N//2 보다 작거나 같은 조합을 만들기
# 조합과 그 역조합을 구하여 노드들이 연결되어있나 확인하기
# 만일 둘다 연결되어있다면, 차이값을 구하여 최소값 확인하기
def combination(idx, count1, selected):
    global result

    if count1 > N//2:
        return

    if idx >= N:
        if 0 < count1:
            tmp1, tmp2 = list(), list()
            for i in range(N):
                if selected[i] == 1:
                    tmp1.append(i + 1)
                else:
                    tmp2.append(i + 1)
            # 노드들이 연결되어있나 확인하는 함수로 넘기기
            tmp_r1, tmp_r2, result1, result2 = check(tmp1), check(tmp2), 0, 0
            if tmp_r1 and tmp_r2:
                for j in tmp1:
                    result1 += population[j-1]
                for k in tmp2:
                    result2 += population[k-1]
                if abs(result1 - result2) < result:
                    result = abs(result1 - result2)
        return

    selected[idx] = 0
    combination(idx + 1, count1, selected)
    selected[idx] = 1
    combination(idx + 1, count1 + 1, selected)


# 연결되어있는지 확인하는 함수
def check(arr):
    # 배열의 길이가 1이라면 True 반환
    if len(arr) == 1:
        return True

    # 배열의 길이가 1 이상 이라면 연결되어있는지 확인, 연결되어있다면 True 반환
    else:
        visited = [0] * (N + 1)
        stack = list()
        stack.append(arr[0])
        while len(stack) > 0:
            r = stack.pop()
            visited[r] = 1
            for c in arr:
                if mat[r][c] == 1 and visited[c] == 0:
                    stack.append(c)
        cnt = 0
        for k in range(N + 1):
            if visited[k] == 1:
                cnt += 1

        # 연결되어있다면, True 반환
        if cnt == len(arr):
            return True

        # 연결되지 않는다면 False 반환
        else:
            return False


N = int(input())
population = list(map(int, input().split()))
lines = [list(map(int, input().split())) for _ in range(N)]

# 연결정보 만들기
mat = [[0]*(N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, lines[i-1][0] + 1):
        mat[i][lines[i-1][j]] = 1

selected= [0] * N
result = 1000000000
combination(0, 0, selected)

if result == 1000000000:
    result = -1

print(result)