import sys
from heapq import *

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

N, M = int(read().rstrip()), int(read().rstrip())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, v = map(int, read().rstrip().split())
    if a != b:
        # 가중치 순서대로 힙을 만들기 때문에 가장 앞에 가중치를 넣어준다.
        graph[a].append([v, a, b])
        graph[b].append([v, b, a])

# 사이클이 생기지 않으려면 이미 한번 거친 노드는
# 다시 거치지 않아야 하기 때문에 visited에 저장
visited_nodes, mst_result = set(), list()
visited_nodes.add(1)
edge_nodes = graph[1][:]
heapify(edge_nodes)

while edge_nodes:
    # edge_nodes들 중에서 가중치의 최솟값을 추출
    value, start, end = heappop(edge_nodes)
    # 방문하지 않은 노드라면 저장, 방문했다고 표시
    if end not in visited_nodes:
        mst_result.append([value, start, end])
        visited_nodes.add(end)
        # 방문한 노드의 연결된 노드들을 모두 edge_nodes에 넣기
        for node in graph[end]:
            heappush(edge_nodes, node)

print(sum([elem[0] for elem in mst_result]))
