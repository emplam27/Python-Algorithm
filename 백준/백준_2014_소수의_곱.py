import sys
from heapq import heappush, heappop

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

K, N = map(int, read().rstrip().split())
numbers = list(map(int, read().rstrip().split()))
result = [*numbers]
tmp = [*numbers]
check = set()

# print(numbers)
# print(result)
# print(tmp)

while len(result) < N:
    for i in range(K):
        candidate = heappop(tmp) * numbers[i]
        if candidate not in check:
            check.add(candidate)
            heappush(tmp, candidate)
            result.append(candidate)

    while len(result) > N:
        result.pop()



    print('numbers', numbers)
    print('result ', result)
    print('tmp    ', tmp)
    print()
# print(numbers)
print(sorted(result))
print(sorted(result)[N - 1])
