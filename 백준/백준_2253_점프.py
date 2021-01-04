import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
stones = [0] * (N + 1)
for _ in range(M):
    stones[int(read().rstrip()) - 1] = -1

print(stones)

stones[2] = 1
result = 0
while True:
    tmp = False
    for i in range(N, 1, -1):
        if stones[i] and stones[i] != -1:
            current_speed = stones[i]
            if i + current_speed + 1 < N and not stones[i + current_speed + 1] and stones[i + current_speed + 1] != -1:
                stones[i + current_speed + 1] = current_speed + 1
                tmp = True
            if i + current_speed < N and not stones[i + current_speed] and stones[i + current_speed] != -1:
                stones[i + current_speed] = current_speed
                tmp = True
            if i + current_speed - 1 < N and not stones[i + current_speed - 1] and stones[i + current_speed - 1] != -1:
                stones[i + current_speed - 1] = current_speed - 1
                tmp = True
    if not tmp:
        break
    print(stones)
