import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

string_A, string_B = list(read().rstrip()), list(read().rstrip())
len_A, len_B = len(string_A), len(string_B)
LCS = [[0] * (len_B + 1) for _ in range(len_A + 1)]

max_result = 0
for i in range(1, len_A + 1):
    for j in range(1, len_B + 1):
        if string_A[i - 1] == string_B[j - 1]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
            if max_result < LCS[i][j]:
                max_result = LCS[i][j]
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])

print(max_result)
