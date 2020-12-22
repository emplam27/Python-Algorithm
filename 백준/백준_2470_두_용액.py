import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

'''
찾아야 하는건 두 특성값 합의 절댓값이 최소가 되는 특성 값이며, 목표값은 0
투포인터를 사용하여 양쪽 끝 값을 더해가면서 최솟값이 되었는가 확인
더한 값이 음수이면 start += 1
더한 값이 양수이면 end -= 1
start == end 까지 반복
'''

N = int(read())
solution = sorted(list(map(int, read().split())))

start, end = 0, N - 1
min_result = float('inf')
result = [0, 0]

while start != end:
    mix = solution[start] + solution[end]
    if abs(mix) < abs(min_result):
        min_result = mix
        result = solution[start], solution[end]

    if mix == 0:
        break
    elif mix < 0:
        start += 1
    else:
        end -= 1

print(*result)