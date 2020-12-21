import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

'''
반지름의 길이가 가장 긴 원부터 정렬 
가장 큰 원부터 배치, 다음 원부터 어떤 원의 내부원인지 판별
어떻게 판별? 
'''

class Circle:
    def __init__(self, index, x, r):
        self.index = index
        self.remain = r * 2
        self.center = x
        self.range = [x - r, x + r]
        self.child = []


N = int(read())
circles = [list(map(int, read().split())) for _ in range(N)]
circles.sort(key=lambda x: x[1], reverse=True)

result = [0] * N

# 가장 큰 원 생성
root_circle = Circle(0, *circles[0])
result[0] = 1

# 원들을 생성하면서 어느원의 자식원인지 결정
for circle_index in range(1, N):
    parent_circle = root_circle
    # print(circles[circle_index])
    child_circle = Circle(circle_index, *circles[circle_index])  # 원을 생성
    result[circle_index] = 1
    while True:
        # print('parent_circle.index', parent_circle.index)
        # print('parent_circle.range', parent_circle.range)
        # print('parent_circle.child', parent_circle.child)
        # print('parent_circle.remain', parent_circle.remain)
        # print('child_circle.center', child_circle.center)
        # 부모원에 자식원이 있다면, 자식원의 자식원으로 들어갈 수 있는지 확인한다.
        # 들어갈 수 있다면, parent, child를 다음 트리로 갱신해준다.
        # 아니라면 부모원의 자식원으로 추가한다.
        flag = False
        if parent_circle.child:
            # 자식원의 자식원으로 포함될 수 있는 경우
            for own_child in parent_circle.child:
                # print('own_child.index', own_child.index)
                # print('own_child.range', own_child.range)
                if own_child.range[0] < child_circle.center < own_child.range[1]:
                    # print('in')
                    # print()
                    parent_circle = own_child
                    flag = True
                    break
        if flag:
            continue

        # 부모의 자식원이거나, 부모원에 자식원이 없다면 자식원을 추가.
        # 자식원의 공간이 1개가 됨. result 갱신
        # 만일 부모원의 remain이 0이 되었다면 공간이 2개가 됨. result 갱신
        parent_circle.child.append(child_circle)
        parent_circle.remain -= child_circle.remain

        if parent_circle.remain == 0:
            result[parent_circle.index] = 2

        # print('parent_circle.child', parent_circle.child)
        # print('parent_circle.remain', parent_circle.remain)
        # print()
        break
# print(result)
print(sum(result) + 1)

