import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline


class Priority_queue:
    def __init__(self):
        self.container = []

    def __len__(self):
        return len(self.container)

    def up_heapify(self, index):
        child_index = index
        while child_index != 0:
            parent_index = (child_index - 1) // 2
            if self.container[parent_index] < self.container[child_index]:
                self.container[parent_index], self.container[child_index] = self.container[child_index], self.container[parent_index]
                child_index = parent_index
            else:
                return

    def down_heapify(self, index):
        parent_index = index
        bigger_child_index = self.find_bigger_child_index(parent_index)
        while parent_index != bigger_child_index:
            self.container[parent_index], self.container[bigger_child_index] = self.container[bigger_child_index], self.container[parent_index]
            parent_index = bigger_child_index
            bigger_child_index = self.find_bigger_child_index(parent_index)

    def find_bigger_child_index(self, index):
        parent = index
        left_child = (parent * 2) + 1
        right_child = (parent * 2) + 2

        if left_child < len(self.container) and self.container[parent] < self.container[left_child]:
            parent = left_child
        if right_child < len(self.container) and self.container[parent] < self.container[right_child]:
            parent = right_child
        return parent

    def heap_pop(self):
        if not len(self.container):
            return 0
        tmp = self.container[0]
        self.container[0] = self.container[-1]
        self.container.pop()
        self.down_heapify(0)
        return tmp


N = int(read())
priority_queue = Priority_queue()
for _ in range(N):
    order = int(read())
    if order != 0:
        priority_queue.container.append(order)
        priority_queue.up_heapify(len(priority_queue) - 1)
    else:
        print(priority_queue.heap_pop())

print(priority_queue.container)