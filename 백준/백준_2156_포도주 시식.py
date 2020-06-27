import sys
sys.stdin = open("input.txt", "r")


def check(idx, value):
    global max_result

    if idx >= N + 1:
        if max_result < value:
            max_result = value
        return

    # 이전에 와인을 마신 상태라면
    if selected[idx - 1]:
        # 현재 와인을 마시지 않고 넘어간다.
        selected[idx] = 0
        check(idx + 1, value)

        # 현재 와인을 마시고 다음 와인을 건너뛴다.
        selected[idx] = 1
        selected[idx + 1] = 0
        check(idx + 2, value + wines[idx])

    # 이전에 와인을 마시지 않은 상태라면
    else:
        # 현재 와인을 마시지않는다.
        selected[idx] = 0
        check(idx + 1, value)

        # 현재 와인을 마신다
        selected[idx] = 1
        check(idx + 1, value + wines[idx])


N = int(input())
wines = [0] + [int(input()) for _ in range(N)] + [0]
selected = [0] * (N + 2)
max_result = 0
check(1, 0)
print(max_result)
