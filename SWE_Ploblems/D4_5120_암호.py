import sys

sys.stdin = open('input.txt', 'r')

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.list_size = 1

    def insert_last(self, data):
        node = self.head
        while True:
            if node.next == None:  # 다음 노드가 없을때까지 이동
                break
            node = node.next
        new_node = Node(data)
        node.next = new_node
        self.list_size += 1

    def insert_data(self):
        node = self.head
        # node = node.next
        for i in range(K):
            for j in range(M-1):
                if node.next == None:
                    node.next = self.head
                node = node.next
            if node.next == None:
                node.next = self.head
            new_node = Node(node.data + node.next.data)
            tmp_next = node.next
            node.next = new_node
            new_node.next = tmp_next
            self.list_size += 1
            node = new_node

    def print_list(self):
        node = self.head
        char = []
        count = 0
        for _ in range(self.list_size):
            char += [node.data]
            node = node.next
        char.reverse()
        print(*char[:10])

for t in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))

    result = LinkedList(arr[0])
    for i in range(1, N):
        result.insert_last(arr[i])

    result.insert_data()
    print('#%d' %t, end=' ')
    result.print_list()