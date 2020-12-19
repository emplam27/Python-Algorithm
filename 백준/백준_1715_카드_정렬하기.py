import sys
import heapq

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

N = int(read())
cards = [int(read()) for _ in range(N)]

result = 0
heapq.heapify(cards)
while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    result += a + b
    heapq.heappush(cards, a + b)
print(result)
