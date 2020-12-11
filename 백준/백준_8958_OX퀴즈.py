import sys

sys.stdin = open('input.txt', 'r')

N = int(input())
answers_list = [list(input()) for _ in range(N)]
result_list = [0] * N
for index, answers in enumerate(answers_list):
    tmp_result = 0
    for answer in answers:
        if answer == 'O':
            tmp_result += 1
            result_list[index] += tmp_result
        else:
            tmp_result = 0

for result in result_list:
    print(result)