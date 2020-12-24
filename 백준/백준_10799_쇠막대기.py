import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline


sticks = list(read().rstrip())
result, stack = 0, []
for index, stick in enumerate(sticks):
    if stick == '(':
        stack.append([stick, index])

    else:
        # 바로 이전에 열린 괄호라면 레이저
        if stack[-1][1] == index - 1:
            stack.pop()
            result += len(stack)

        # 아니라면 쇠막대기
        else:
            stack.pop()
            result += 1

print(result)