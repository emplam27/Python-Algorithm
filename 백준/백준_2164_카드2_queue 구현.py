import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline


class Queue:
    def __init__(self, capacity):
        self.length = 0
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0

    def my_enque(self, num):
        self.queue[self.rear] = num
        self.rear += 1
        self.length += 1

    def my_deque(self):
        if self.length == 0:
            return -1
        tmp = self.queue[self.front]
        self.front += 1
        self.length -= 1
        return tmp

    def __len__(self):
        return self.length


N = int(read())
queue = Queue(5000001)
for i in range(1, N + 1):
    queue.my_enque(i)

while len(queue) > 1:
    queue.my_deque()
    if len(queue) == 1:
        break
    tmp = queue.my_deque()
    queue.my_enque(tmp)
print(queue.queue[queue.front])
