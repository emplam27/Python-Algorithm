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

    def search_index_insert(self, arr):
        node = self.head
        count = 0
        if node.data > arr[0]:
            for i in range(N):
                self.insert_first(arr[i])
            return
        while True:
            if count > self.list_size:
                break
            if node.next == None:
                for i in range(N):
                    self.insert_last(arr[i])
                return
            elif node.next.data > arr[0]:
                break
            node = node.next
            count += 1
        for i in range(len(arr)):
            new_node = Node(arr[i])
            tmp_next = node.next
            node.next = new_node
            new_node.next = tmp_next
            self.list_size += 1
            node = new_node

    def insert_first(self, data):
        new_node = Node(data)       # 새로운 Node
        tmp_node = self.head        # 기존의 head 잠시 보관
        self.head = new_node        # head를 새로운 노드로 변경
        self.head.next = tmp_node   # head에 이어지는 요소를 기존 head로 변경
        self.list_size += 1

    def insert_last(self, data):
        node = self.head
        while True:
            if node.next == None:   # 다음 노드가 없을때까지 이동
                break
            node = node.next

        new_node = Node(data)
        node.next = new_node
        self.list_size += 1

    def print_list(self):
        node = self.head
        char = ''
        while node:
            char += str(node.data)
            char += ' '
            node = node.next
        print(char)

    def print_list_10(self):
        node = self.head
        char = []
        count = 0
        while count < self.list_size:
            if count > (self.list_size - 11):
                char += [node.data]
            node = node.next
            count += 1
        char.reverse()
        print(*char)



for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]

    result = LinkedList(arr[0][0])
    for i in range(1, N):
        result.insert_last(arr[0][i])

    for i in range(1, M):
        result.search_index_insert(arr[i])

    print('#%d' %t, end=' ')
    result.print_list_10()