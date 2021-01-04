import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline


N, K = map(int, read().rstrip().split())
products = list(map(int, read().rstrip().split()))
orders = dict()
for index, product in enumerate(products):
    tmp = orders.get(product, deque())
    tmp.append(index)
    orders[product] = tmp

plugs, result = [0] * N, 0
for product in products:
    candi_plug_index, max_distance, priority = 0, 0, -1
    for plug_index, plug in enumerate(plugs):

        # 현재 플러그와 같은 플러그가 있다면 바로 사용
        if product == plug:
            break

        # 플러그가 비어있다면 바로 사용
        elif not plug:
            plugs[plug_index] = product
            break

        # 플러그가 비어있지 않고, 해당 전자기기는 더 이상 사용되지 않는다면 우선순위 후보로 지정
        elif priority == -1 and not orders[plug]:
            priority = plug_index

        # 플러그가 비어있지 않고, 사용하는 플러그 중 가장 멀리 있다면 후보 갱신
        elif priority == -1 and max_distance < orders[plug][0]:
            max_distance = orders[plug][0]
            candi_plug_index = plug_index

    else:
        # 우선순위 후보가 없다면 후보로 선정된 플러그를 교체
        if priority == -1:
            plugs[candi_plug_index] = product
        # 우선순위 후보가 있다면 교체
        else:
            plugs[priority] = product
        result += 1
    # 교체된 플러그를 순서에서 빼주기
    orders[product].popleft()

print(result)
