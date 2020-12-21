import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

'''
circle_stack에 원들을 저장한다. 저장할 때 자식이 있는지, 자식원들에 의해 지름이 꽉 차는지 저장한다.

자식원들에 의해 꽉 찬 원은 2개 영역으로 나눠진다. 이외에는 1개 영역이다.
'''

def close_circle(current_point):
    global result

    # 원을 닫는데, 자식원과 공간이 남아있었다면 remain = True
    if current_point != circle_stack[-1]['left'] and current_point < circle_stack[-1]['right']:
        circle_stack[-1]['remain'] = True

    # 자식원이 있었는지 여부와 원이 꽉 찼었는지 여부를 확인하여 결과값 갱신
    if not circle_stack[-1]['child'] and not circle_stack[-1]['remain']:
        result += 1
    elif circle_stack[-1]['child'] and not circle_stack[-1]['remain']:
        result += 2
    else:
        result += 1

    # 스택에서 해당 원 빼주기
    tmp = circle_stack[-1]['right']
    circle_stack.pop()
    return tmp


N = int(read())
circles = list()
for _ in range(N):
    circle = list(map(int, read().split()))
    circles.append((circle[0] - circle[1], circle[0] + circle[1]))

circles.sort(key=lambda x: x[1])
circles.sort(key=lambda x: x[0], reverse=True)

circle_stack = []
current_point = circles[-1][0]
result = 1
index = N - 1
while circle_stack or index >= 0:

    # 스택에 원이 존재하지 않는다면 해당 원을 추가해준다.
    if not circle_stack:
        circle_stack.append(dict({'left': circles[index][0], 'right': circles[index][1], 'remain': False, 'child': False}))
        current_point = circles[index][0]
        index -= 1
        continue

    # current_point와 circle_stack[-1]['right']이 같으면 원을 닫아준다.
    if current_point == circle_stack[-1]['right']:
        current_point = close_circle(current_point)
        continue

    # 스택에 원이 존재한다면 자식원을 만드는지, 현재의 원을 닫는지 확인한다.
    # 자식원을 추가하는데 current_point와 비교하여 공백이 없다면 스택에 추가한다.
    if current_point == circles[index][0]:
        circle_stack[-1]['child'] = True
        circle_stack.append(dict({'left': circles[index][0], 'right': circles[index][1], 'remain': False, 'child': False}))
        index -= 1
        continue

    # 자식원을 추가하는데 current_point와 비교하여 공백이 있다면 부모원의 remain을 True로 바꾼다.
    if current_point < circles[index][0] and circles[index][1] <= circle_stack[-1]['right']:
        circle_stack[-1]['remain'] = True
        circle_stack.append(dict({'left': circles[index][0], 'right': circles[index][1], 'remain': False, 'child': False}))
        current_point = circles[index][0]
        index -= 1
        continue

    # 원이 닫힌다면 해당 원의 remain을 확인하여 False라면 + 2, True라면 + 1 해준다.
    # 해당 원을 스택에서 삭제하고 다음 원을 스택에 넣어준다.
    else:
        current_point = close_circle(current_point)
        continue
print(result)