import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

'''
DP[start][end]는 start 행렬부터 end 행렬까지의 곱셈 중 가장 최소값을 저장
<점화식>
DP[start][end] = min(DP[start][end], DP[start][middle] + DP[middle + 1][end] + 두 행렬의 곱셈 값)   
중간값인 middle은 start와 end 사이의 값이 들어가게 하며, (start ~ middle, middle + 1 ~ end)로 나눈다. 

만일 N = 5인 DP를 만든다면 순회 과정은 대각선 아래방향
DP[0][1] => DP[1][2] => DP[2][3] => DP[3][4] => DP[0][2] => DP[1][3] => DP[2][4] => DP[0][3] => DP[1][4] => DP[0][4] 
'''

N = int(read().rstrip())
matrix = [list(map(int, read().rstrip().split())) for _ in range(N)]
DP = [[0] * N for _ in range(N)]

# 대각선 아래방향으로 순회할 수 있게 시작값과 끝값을 정하기
for gap in range(1, N):
    for start in range(N - gap):
        end = start + gap
        # 무한대값으로 초기화해주기
        DP[start][end] = float('inf')
        # middle 값으로 start와 end 사이값을 넣어주기
        for middle in range(start, end):
            DP[start][end] = min(DP[start][end], DP[start][middle] + DP[middle + 1][end]
                                 + (matrix[start][0] * matrix[middle][1] * matrix[end][1]))

print(DP[0][N - 1])
