import sys

# 표준 입/출력 : 콘솔입출력
sys.stdin = open("input.txt", "r")  # 파일입력

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [input().split() for _ in range(N)]

    char = []
    for ci, ki in arr:
        ki = int(ki)
        for i in range(ki):
            char += ci

    print('#%d' %t)
    idx = 0
    while idx < len(char):
        print(char[idx], end='')
        idx += 1
        if idx % 10 == 0:
            print()
    print()

        # print(ci, end='')
        #
        # if count == 0
        # print()