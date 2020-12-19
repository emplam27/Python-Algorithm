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

    def my_push(self, num):
        self.queue[self.rear] = num
        self.rear += 1
        self.length += 1
        if self.rear == self.capacity:
            self.rear = 0

    def my_pop(self):
        if self.length == 0:
            return -1
        tmp = self.queue[self.front]
        self.front += 1
        self.length -= 1
        if self.front == self.capacity:
            self.front = 0
        return tmp

    def my_size(self):
        return self.length

    def my_empty(self):
        if self.length:
            return 0
        else:
            return 1

    def my_front(self):
        if not self.length:
            return -1
        else:
            return self.queue[self.front]

    def my_back(self):
        if not self.length:
            return -1
        if self.rear != 0:
            return self.queue[self.rear - 1]
        else:
            return self.queue[self.capacity - 1]


N = int(read())
orders = [list(read().split()) for _ in range(N)]

my_queue = Queue(20000000)
for order in orders:
    if order[0] == 'push':
        my_queue.my_push(int(order[1]))
    elif order[0] == 'pop':
        print(my_queue.my_pop())
    elif order[0] == 'size':
        print(my_queue.my_size())
    elif order[0] == 'empty':
        print(my_queue.my_empty())
    elif order[0] == 'front':
        print(my_queue.my_front())
    else:
        print(my_queue.my_back())

