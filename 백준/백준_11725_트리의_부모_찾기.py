import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

'''
그래프 노드의 수가 십만개이기 때문에 딕셔너리를 활용하여 그래프 만들기
그래프 그린 후, 1번 노드부터 DFS 탐색을 통해 부모노드 구해서 저장하기
'''

N = int(read().rstrip())
graph = dict()
for _ in range(N - 1):
    node_a, node_b = map(int, read().rstrip().split())
    graph[node_a] = graph.get(node_a, []) + [node_b]
    graph[node_b] = graph.get(node_b, []) + [node_a]

results = [0] * (N + 1)
stack = list()
stack.append(1)
visited = [0] * (N + 1)
visited[1] = 1
while stack:
    current_node = stack.pop()
    for next_node in graph[current_node]:
        if not visited[next_node]:
            results[next_node] = current_node
            visited[next_node] = 1
            stack.append(next_node)

for result in results[2:]:
    print(result)
