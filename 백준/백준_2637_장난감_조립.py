import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

'''
기본부품부터 완제품까지의 방향성 그래프를 그린 후, 위상정렬을 실시하여 어떤 부품이 몇개 필요한지를 전달하자.
'''

N = int(read().rstrip())
M = int(read().rstrip())
graph = dict()
# [현재 나를 가리키고 있는 부품의 수(진입차수) int, 내가 가리키고 있는 부품들 set, 나를 만들기 위해 필요한 부품정보 dict]
for _ in range(M):
    bigger, smaller, count = map(int, read().rstrip().split())
    # 작은 부품 정보 갱신
    smaller_value = graph.get(smaller, [0, set(), dict()])
    smaller_value[1].add(bigger)
    graph[smaller] = smaller_value
    # 큰 부품 정보 갱신
    bigger_value = graph.get(bigger, [0, set(), dict()])
    bigger_value[0] += 1
    bigger_value[2][smaller] = count
    graph[bigger] = bigger_value

while len(graph) > 1:
    for key, value in graph.items():
        if not value[0]:
            for node in value[1]:
                graph[node][0] -= 1
                # 현재 부품이 가리키고 있는 부품들은 해당 부품을 몇 개 필요로 하는지 확인하고, 해당 부품을 구성하는 부품 목록을 곱하여 넘겨줌
                if value[2]:
                    require_count = graph[node][2][key]
                    for part_key, part_value in value[2].items():
                        graph[node][2][part_key] = graph[node][2].get(part_key, 0) + require_count * part_value
                    graph[node][2].pop(key)
            graph.pop(key)
            break

for part in sorted(graph[N][2].items()):
    print(*part)


