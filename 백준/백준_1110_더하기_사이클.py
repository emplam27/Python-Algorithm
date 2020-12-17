import sys

sys.stdin = open('input.txt', 'r')


N = int(input())

num, count = N, 1
while True:
    sum_num = num if num < 10 else num // 10 + num % 10
    new_num = ((num % 10) * 10) + (sum_num % 10)
    if N == new_num:
        print(count)
        break
    count += 1
    num = new_num
