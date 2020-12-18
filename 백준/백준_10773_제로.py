import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

K = int(read())
orders = [int(read()) for _ in range(K)]

result = []
for order in orders:
    if not order:
        result.pop()
    else:
        result.append(order)

print(sum(result))