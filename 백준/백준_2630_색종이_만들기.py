import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline


def check_paper(piece, size):
    global result

    # print('piece:', piece, 'size:', size)
    if size == 1:
        result[piece[0][0]] += 1
        return

    piece_sum = sum([sum(val) for val in piece])
    if piece_sum == 0 or piece_sum == size ** 2:
        result[piece[0][0]] += 1
        # print('result', result)
        return

    for r in range(2):
        for c in range(2):
            tmp = []
            for k in range(size // 2):
                tmp.append(piece[(size // 2) * r + k][(size // 2) * c:(size // 2) * (c + 1)])
            check_paper(tmp, size // 2)


N = int(read())
paper = [list(map(int, read().split())) for _ in range(N)]
result = [0, 0]
check_paper(paper, N)
print(result[0])
print(result[1])
