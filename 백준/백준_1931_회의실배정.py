import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

'''
가장 빨리 끝나는 회의를 고려한다.
(종료시간, 시작시간)을 기준으로 정렬하여 최대 갯수를 구한다.
'''

N = int(read().rstrip())
times = sorted([list(map(int, read().rstrip().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))
stack = list()
stack.append(times[0])
for i in range(1, N):
    if stack[-1][1] <= times[i][0]:
        stack.append(times[i])
print(stack)
