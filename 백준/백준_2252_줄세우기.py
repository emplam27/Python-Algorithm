import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

'''
위상정렬을 사용하여 작은 순서부터 줄을 세운다.

1. 방향 그래프에서 본인을 가르키고있는 노드를 찾는다. 해당 노드는 우선순위의 가장 위에 있다고 할 수 있다.
2. 해당 노드를 삭제하고, 그 노드가 가르키고 있던 방향성 역시 삭제한다. 다시 위 과정을 반복한다.
'''

N, M = map(int, read().rstrip().split())
graph = dict()
for _ in range(M):
    smaller, bigger = map(int, read().rstrip().split())
    # 작은 노드는 해당 노드가 어떤 노드를 가르키고 있는지 저장
    smaller_value = graph.get(smaller, [0, []])
    smaller_value[1].append(bigger)
    graph[smaller] = smaller_value
    # 큰 노드는 해당 노드를 몇개의 노드가 가르키고 있는지 저장
    bigger_value = graph.get(bigger, [0, []])
    bigger_value[0] += 1
    graph[bigger] = bigger_value

# 어떤 노드와도 연결되어 있지 않다면 정보를 알 수 없으므로 바로 결과값에 추가
result = [i for i in range(1, N + 1) if i not in graph]

# 위상정렬 수행
while graph:
    for smaller_node, (value, bigger_nodes) in graph.items():
        if not value:
            result.append(smaller_node)
            for node in bigger_nodes:
                graph[node][0] -= 1
            graph.pop(smaller_node)
            break
            
print(*result)
