import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline


def up_heapify(index, queue):
    child_index = index
    while child_index != 0:
        parent_index = (child_index - 1) // 2
        if queue[parent_index] < queue[child_index]:
            queue[parent_index], queue[child_index] = queue[child_index], queue[parent_index]
            child_index = parent_index
        else:
            return


def find_bigger_child_index(index, heap_size):
    parent = index
    left_child = (parent * 2) + 1
    right_child = (parent * 2) + 2

    if left_child < heap_size and priority_queue[parent] < priority_queue[left_child]:
        parent = left_child
    if right_child < heap_size and priority_queue[parent] < priority_queue[right_child]:
        parent = right_child
    return parent


def down_heapify(index, queue):
    parent_index = index
    bigger_child_index = find_bigger_child_index(parent_index, len(queue))
    while parent_index != bigger_child_index:
        queue[parent_index], queue[bigger_child_index] = queue[bigger_child_index], queue[parent_index]
        parent_index = bigger_child_index
        bigger_child_index = find_bigger_child_index(parent_index, len(queue))


def heap_pop(queue):
    if not len(queue):
        return 0
    tmp = priority_queue[0]
    priority_queue[0] = priority_queue[-1]
    priority_queue.pop()
    down_heapify(0, queue)
    return tmp


N = int(read())
priority_queue = []
for _ in range(N):
    order = int(read())
    if order != 0:
        priority_queue.append(order)
        up_heapify(len(priority_queue) - 1, priority_queue)
    else:
        print(heap_pop(priority_queue))
