import sys

sys.stdin = open("input.txt", "r")
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 단조증가수가 되는지 검사할 숫자를 만든다.
    max_num = 0
    for i in range(N-1):
        for j in range(i + 1, N):
            result = 1
            num = arr[i] * arr[j]
            num_char = str(num)

            # 단조증가 되는지 확인한다.
            for k in range(len(num_char) - 1):
                if int(num_char[k]) > int(num_char[k+1]):
                    num = 0
                    break

            # 단조증가 됐을 때, 가장 큰 값이면 저장한다.
            if num > max_num:
                max_num = num

    if max_num != 0:
        print('#%d' % t, max_num)
    else:
        print('#%d' % t, -1)
