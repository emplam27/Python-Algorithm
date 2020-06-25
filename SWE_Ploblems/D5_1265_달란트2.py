# 1 36
# 2 1024
# 3 46656
# 4 1679616
# 5 26214400
# 6 2448880128
# 7 125524238436
# 8 2821109907456
# 9 162679413013056
# 10 5856458868470016

import sys

sys.stdin = open("input2.txt", "r")

'''
묶음은 N//P와 N//P + 1이 가장 효율적일 것 같다.
'''

for t in range(1, int(input()) + 1):
    N, P = map(int, input().split())

    lower_num = N // P
    for i in range(P, -1, -1):
        if (lower_num * i) + ((lower_num + 1) * (P - i)) == N:
            print('#{} {}'.format(t, (lower_num ** i) * ((lower_num + 1) ** (P - i))))
            break
