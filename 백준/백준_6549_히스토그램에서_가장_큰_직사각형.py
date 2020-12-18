import sys

sys.stdin = open('input.txt', 'r')

while True:
    input_value = list(map(int, input().split()))
    if not input_value[0]:
        break

    N = input_value[0]
    squares = input_value[1:]
    print(N, squares)


