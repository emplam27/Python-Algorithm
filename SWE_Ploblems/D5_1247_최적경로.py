import sys
sys.stdin = open('input.txt', 'r')


def permutiation(idx, value, prev_x, prev_y):
    global min_result

    if value > min_result:
        return

    if idx == N:
        tmp_result = value + (abs(end_x - prev_x) + abs(end_y - prev_y))
        if min_result > tmp_result:
            min_result = tmp_result
        return

    for i in range(N):
        if selected[i] == 0:
            selected[i] = 1
            tmp = (abs(customers[i][0] - prev_x) + abs(customers[i][1] - prev_y))
            permutiation(idx + 1, value + tmp, customers[i][0], customers[i][1])
            selected[i] = 0


for t in range(1, int(input()) + 1):
    N = int(input())
    points = list(map(int, input().split()))
    start_x, start_y = points[0], points[1]
    end_x, end_y = points[2], points[3]

    customers = []
    for i in range(4, len(points), 2):
        customers.append([points[i], points[i + 1]])

    min_result = 2**31
    selected = [0] * N
    permutiation(0, 0, start_x, start_y)

    print('#%d' %t, min_result)
