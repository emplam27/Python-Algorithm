import sys

sys.stdin = open("input.txt", "r")


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, data):
        new_node = Node(data)
        self.head = new_node
        self.list_size = 1

    def insert_last(self, data):
        node = self.head
        while True:
            if node.next == None:   # 다음 노드가 없을때까지 이동
                break
            node = node.next

        new_node = Node(data)
        node.next = new_node
        self.list_size += 1

    def insert_index(self, index, data):
        node = self.head
        current = 1
        while current < index:
            node = node.next
            current += 1

        new_node = Node(data)
        tmp_next = node.next
        node.next = new_node
        new_node.next = tmp_next
        self.list_size += 1

    # index 로 data 찾기
    def search_node(self, index):
        node = self.head
        current = 0
        while current < index:
            node = node.next
            current += 1
        char = str(node.data)
        return char

    def print_list(self):
        node = self.head
        char = ''
        while node:
            char += str(node.data)
            node = node.next
        print(char)

for t in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))
    plus = [list(map(int, input().split())) for _ in range(M)]

    result_list = LinkedList(arr[0])
    for i in range(1, len(arr)):
        result_list.insert_last(arr[i])


    for i, j in plus:
        result_list.insert_index(i, j)

    print('#%d' %t, result_list.search_node(L))
