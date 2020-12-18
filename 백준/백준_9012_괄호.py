import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

T = int(input())
for _ in range(T):
    PS = list(input())

    stack = []
    for ps in PS:
        if not stack:
            stack.append(ps)
        elif stack[-1] == '(' and ps == ')':
            stack.pop()
        else:
            stack.append(ps)

    if stack:
        print('NO')
    else:
        print('YES')
