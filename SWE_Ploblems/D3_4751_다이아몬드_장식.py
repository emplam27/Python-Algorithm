import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T + 1):
    word = str(input())

    #       ..#. * i-1 + ..#..
    #       .#.# * i-1 + .#.#.
    #       #.{word}. * i-1 + #.{word}.#
    #       .# .# * i-1 + .#.#.
    #       ..# . * i-1 + ..#..

    result1 = ''
    result2 = ''
    result3 = ''
    result4 = ''
    result5 = ''


    for i in word:
        result1 += '..#.'
        result2 += '.#.#'
        result3 += '#.' + i + '.'
        result4 += '.#.#'
        result5 += '..#.'

    result1 += '.'
    result2 += '.'
    result3 += '#'
    result4 += '.'
    result5 += '.'

    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)






