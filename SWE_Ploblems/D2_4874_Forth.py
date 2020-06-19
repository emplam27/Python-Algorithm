import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T + 1):
    arr = list(input().split())
    operator = ['+', '-', '*', '/', '.']
    result = ''
    stack = []

    for i in range(len(arr)):
        if arr[i] not in operator:
            stack.append(int(arr[i]))
            continue

        elif arr[i] == '.':
            if len(stack) == 1:
                result = str(stack[-1])
                break
            else:
                result = 'error'
                break


        else:
            if len(stack) >= 2:
                tmp2 = stack.pop()
                tmp = stack.pop()
                if tmp not in operator and tmp2 not in operator:
                    if arr[i] == '+':
                        stack.append(tmp + tmp2)
                        continue
                    if arr[i] == '-':
                        stack.append(tmp - tmp2)
                        continue
                    if arr[i] == '*':
                        stack.append(tmp * tmp2)
                        continue
                    if arr[i] == '/':
                        if tmp2 == 0:
                            result = 'error'
                            break
                        else:
                            stack.append(int(tmp / tmp2))
                            continue
                else:
                    result = 'error'
                    break
            else:
                result = 'error'
                break

    print('#%d' % t, result)
