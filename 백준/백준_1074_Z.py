import sys

sys.stdin = open('input.txt', 'r')


def z_move(size, r_location, c_location):
    global number, r, c

    if size == 2:
        if r_location - 2 <= r <= r_location - 1 and c_location - 2 <= c <= c_location - 1:
            if r == r_location - 2 and c == c_location - 2:
                print(number)
            elif r == r_location - 2 and c == c_location - 1:
                print(number + 1)
            elif r == r_location - 1 and c == c_location - 2:
                print(number + 2)
            else:
                print(number + 3)
            exit()
        number += 4
        return
    size = size // 2
    z_move(size, r_location - size, c_location - size)
    z_move(size, r_location - size, c_location)
    z_move(size, r_location, c_location - size)
    z_move(size, r_location, c_location)


N, r, c = map(int, input().split())
number = 0
z_move(2 ** N, 2 ** N, 2 ** N)
