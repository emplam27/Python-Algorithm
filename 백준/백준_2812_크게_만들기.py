import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline


N, K = map(int, read().strip().split())
numbers = list(list(read().strip()))

stack, delete_count = [], K
for number in numbers:
    while stack and delete_count > 0 and stack[-1] < number:
        stack.pop()
        delete_count -= 1
    stack.append(number)
print(''.join(stack[:N - K]))
