import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline


class stack:
    def __init__(self):
        self.arr = []
        self.length = 0

    def my_push(self, num):
        self.arr.append(num)
        self.length += 1

    def my_pop(self):
        if self.length:
            tmp = self.arr[-1]
            self.arr = self.arr[:-1]
            self.length -= 1
            return tmp
        else:
            return -1

    def my_size(self):
        return self.length

    def my_empty(self):
        if self.length:
            return 0
        else:
            return 1

    def my_top(self):
        if self.length:
            return self.arr[-1]
        else:
            return -1


N = int(input())
orders = [ list(input().split()) for _ in range(N)]
my_stack = stack()
for order in orders:
    if order[0] == 'push':
        my_stack.my_push(order[1])
    elif order[0] == 'pop':
        print(my_stack.my_pop())
    elif order[0] == 'size':
        print(my_stack.my_size())
    elif order[0] == 'empty':
        print(my_stack.my_empty())
    elif order[0] == 'top':
        print(my_stack.my_top())


