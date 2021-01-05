import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

'''
1차원 배열에 set을 넣어서 해당 구간마다 도착 가능한 속도들을 저장한다.
첫번째 점프로 갈수있는 경우를 모두 구하고, 두번째 점프로 갈 수 있는 경우를 모두 구하고.. 
'''


def check_jump(step, speed):
    tmp = False
    if step + speed <= N and speed > 0:
        if not stones[step + speed]:
            stones[step + speed].add(speed)
            tmp = True
        elif stones[step + speed] and (speed not in stones[step + speed]) and -1 not in stones[
            step + speed]:
            stones[step + speed].add(speed)
            tmp = True
    return tmp


N, M = map(int, read().rstrip().split())
stones = [set() for _ in range(N + 1)]
for _ in range(M):
    stones[int(read().rstrip())].add(-1)

result = 1
stones[2].add(1)
while True:
    flag = False
    for current_step in range(N, 1, -1):
        for current_speed in stones[current_step]:
            if current_speed <= 0:
                continue
            if check_jump(current_step, current_speed + 1):
                flag = True
            if check_jump(current_step, current_speed):
                flag = True
            if check_jump(current_step, current_speed - 1):
                flag = True
    result += 1
    print(stones)
    if stones[N] or not flag:
        break

if not stones[N]:
    print(-1)
else:
    print(result)
