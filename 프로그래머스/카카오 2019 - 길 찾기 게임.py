"""
2진트리 만들기
전위순회, 후위순회 실시
2진트리에서의 중위순회는 정렬과 같다.
"""

import sys
sys.setrecursionlimit(10000)


class node:
    def __init__(self, x, num):
        self.value = x
        self.number = num
        self.left = None
        self.right = None


def solution(nodeinfo):
    def preorder(node):
        if not node: return
        pre_result.append(node.number)
        preorder(node.left)
        preorder(node.right)

    def postorder(node):
        if not node: return
        postorder(node.left)
        postorder(node.right)
        post_result.append(node.number)

    for index, info in enumerate(nodeinfo):
        info.append(index + 1)
    nodeinfo.sort(key=lambda node: node[1], reverse=True)

    root_node = node(nodeinfo[0][0], nodeinfo[0][2])
    for x, y, num in nodeinfo[1:]:
        cur_node, new_node = root_node, node(x, num)
        while True:
            if cur_node.value > new_node.value:
                # 왼쪽 자식노드로 이동
                if not cur_node.left:
                    cur_node.left = new_node
                    break
                else:
                    cur_node = cur_node.left
            else:
                # 오른쪽 자식노드로 이동
                if not cur_node.right:
                    cur_node.right = new_node
                    break
                else:
                    cur_node = cur_node.right

    pre_result, post_result = [], []
    preorder(root_node)
    postorder(root_node)

    return [pre_result, post_result]


print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
