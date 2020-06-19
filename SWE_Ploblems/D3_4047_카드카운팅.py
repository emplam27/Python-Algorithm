import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T + 1):
    info = str(input())
    a = len(info) // 3
    S_cnt = 13
    D_cnt = 13
    H_cnt = 13
    C_cnt = 13
    result = ''

    for i in range(a):
        if info[3*i:3*i + 3] in info[3*(i+1):]:
            result = 'ERROR'
            break
        else:
            if info[3 * i] == 'S':
                S_cnt -= 1
            elif info[3 * i] == 'D':
                D_cnt -= 1
            elif info[3 * i] == 'H':
                H_cnt -= 1
            else :
                C_cnt -= 1

    if 'ERROR' in result:
        print('#%d' % t, 'ERROR')
    else:
        print('#%d' %t, S_cnt, D_cnt, H_cnt, C_cnt)



