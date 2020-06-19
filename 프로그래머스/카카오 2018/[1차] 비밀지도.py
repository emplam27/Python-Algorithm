def solution(n, arr1, arr2):
    answer = [''] * n

    for i in range(n):
        tmp1, tmp2 = arr1[i], arr2[i]
        tmp_str1, tmp_str2 = '', ''
        for j in range(n - 1, -1, -1):
            if tmp1 // (2 ** j) == 1:
                tmp_str1 += '1'
                tmp1 -= (2 ** j)
            else:
                tmp_str1 += '0'
            if tmp2 // (2 ** j) == 1:
                tmp_str2 += '1'
                tmp2 -= (2 ** j)
            else:
                tmp_str2 += '0'
        arr1[i] = tmp_str1
        arr2[i] = tmp_str2

    for i in range(n):
        for j in range(n):
            if arr1[i][j] == '0' and arr2[i][j] == '0':
                answer[i] += ' '
            else:
                answer[i] += '#'

    return answer
