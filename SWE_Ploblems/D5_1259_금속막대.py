import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    bolt = list(map(int, input().split()))

    index = [0] * max(bolt)
    result = []

    # 어떤 값의 수나사와 암나사가 각각 1개씩만 나오면, 그 둘이 처음과 끝이 됨
    for i in range(len(bolt)):
        index[bolt[i]-1] += 1

    # 인덱스를 이용하여 1개씩 있는 수나사, 암나사의 값을 찾음
    odd_idx = []
    for i in range(len(bolt)):
        if index[bolt[i]-1] % 2 == 1:
            odd_idx.append(bolt[i])

    # 첫 시작 나사를 고정
    for i in range(N):
        if bolt[2 * i] in odd_idx:
            result.append(bolt[2 * i])
            result.append(bolt[2 * i + 1])

    # 첫 나사에 다른 나사들을 붙여봄
    for i in range(N):
        for j in range(N):
            if result[2 * i + 1] == bolt[2 * j]:
                result.append(bolt[2 * j])
                result.append(bolt[2 * j + 1])

    result_char = ''
    for i in range(len(result)):
        result_char = result_char + '%d' % result[i] + ' '
    print('#%d' % t, result_char[:-1])