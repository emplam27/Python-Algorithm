import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

'''
[현재 노드의 가중치 int, 나의 부모노드 int, 해당 노드가 가지고 있는 가지들의 가중치 list(역순정렬)]
'''

N = int(read().rstrip())

tree = dict()
tree[0] = [0, 0, [0]]
for _ in range(N - 1):
    bigger, smaller, weight = map(int, read().rstrip().split())

    # 자식노드 값 입력
    smaller_value = tree.get(smaller, [0, 0, [0]])
    smaller_value[0] = weight
    smaller_value[1] = bigger
    tree[smaller] = smaller_value

    # 부모노드 값 입력
    tree[bigger] = tree.get(bigger, [0, 0, [0]])

max_radius = 0
for node in range(N, 0, -1):
    if node in tree:
        current_node_weight, parent_node, node_weight_list = tree[node]

        # 해당 노드가 가지고 있는 가지들의 가중치들 중 가장 큰 2개의 가중치를 더해 결과값으로 전해준다.
        if len(node_weight_list) >= 2:
            node_weight_list.sort(reverse=True)
            max_radius = max(max_radius, (node_weight_list[0] + node_weight_list[1]))

        # 현재 노드의 부모노드에게 현재 노드의 가중치 + 해당 노드가 가지고 있는 가지들의 가중치들의 조합을 전달해준다.
        max_weight = node_weight_list[0]
        tree[parent_node][2].append((current_node_weight + max_weight))

print(max_radius)
