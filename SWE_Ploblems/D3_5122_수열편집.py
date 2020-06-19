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

    # 리스트의 앞에 요소를 추가하는 메서드
    def insert_first(self, data):
        new_node = Node(data)  # 새로운 Node
        tmp_node = self.head  # 기존의 head 잠시 보관
        self.head = new_node  # head를 새로운 노드로 변경
        self.head.next = tmp_node  # head에 이어지는 요소를 기존 head로 변경
        self.list_size += 1

    # 리스트의 중간에 요소를 추가하는 메서드
    def insert_index(self, index, data):
        if index == 0:
            self.insert_first(data)
            return
        node = self.head
        current = 0
        while current < index:
            node = node.next
            current += 1
        new_node = Node(data)
        tmp_next = node.next
        node.next = new_node
        new_node.next = tmp_next
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

    # index 로 data 찾기
    def search_node(self, index):
        if self.list_size < index:
            return -1
        node = self.head
        current = 0
        while current < index:
            node = node.next
            current += 1
        return node.data

    def replace_node(self, index, data):
        node = self.head
        current = 0
        while current < index:
            node = node.next
            current += 1
        node.data = data

    # index 노드 지우기
    def delete_node(self, index):
        if self.list_size < 1:
            return  # Underflow
        elif self.list_size < index:
            return  # Overflow

        if index == 0:
            node = self.head
            self.head = node.next
            del node
            self.list_size -= 1
            return
        node = self.head
        current = 0
        while current < index-1:
            node = node.next
            current += 1
        node.next = node.next.next
        del_node = node.next
        del del_node
        self.list_size -= 1




for t in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))
    plus = [list(input().split()) for _ in range(M)]

    result_list = LinkedList(arr[0])
    for i in range(1, len(arr)):
        result_list.insert_last(arr[i])

    for i in range(M):
        if plus[i][0] == 'I':
            result_list.insert_index(int(plus[i][1]), int(plus[i][2]))

        elif plus[i][0] == 'D':
            result_list.delete_node(int(plus[i][1]))

        elif plus[i][0] == 'C':
            result_list.replace_node(int(plus[i][1]), int(plus[i][2]))

    print('#%d' %t, result_list.search_node(L))
