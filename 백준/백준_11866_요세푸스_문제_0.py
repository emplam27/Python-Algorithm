import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline


class Queue:
    def __init__(self, capacity):
        self.length = 0
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.capacity = capacity

    def my_enque(self, num):
        if self.rear == self.capacity:
            self.rear = 0
        self.queue[self.rear] = num
        self.rear += 1
        self.length += 1

    def my_deque(self):
        if self.length == 0:
            return -1
        tmp = self.queue[self.front]
        self.front += 1
        self.length -= 1
        if self.front == self.capacity:
            self.front = 0
        return tmp

    def __len__(self):
        return self.length


N, K = map(int, read().split())

queue = Queue(1000)
for i in range(1, N + 1):
    queue.my_enque(i)

result, count = [], 1
while len(queue):
    if count % K != 0:
        queue.my_enque(queue.my_deque())
    else:
        result.append(str(queue.my_deque()))
    count += 1
print('<' + ', '.join(result) + '>')



