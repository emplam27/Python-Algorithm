import sys

sys.stdin = open('input.txt', 'r')


def check(value):
    global N, result

    if value >= N:
        if value == N:
            result += 1
        return

    check(value + 1)
    check(value + 2)
    check(value + 3)


T, results = int(input()), []
for _ in range(T):
    N, result = int(input()), 0
    check(0)
    results.append(result)
for i in range(T):
    print(results[i])
