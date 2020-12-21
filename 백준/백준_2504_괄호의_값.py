import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline


def _quit():
    print(0)
    exit()


brackets = list(read().strip())
print(brackets)

tmp = [0] * 31
number_stack = []
bracket_stack = []
depth, result = 0, 1
for bracket in brackets:
    if bracket == '(' or bracket == '[':
        if result != 1:
            tmp[depth] += result
            result = 1
        bracket_stack.append(bracket)
        if bracket == '(':
            number_stack.append(2)
        else:
            number_stack.append(3)
        depth += 1

    else:
        if not bracket_stack:
            _quit()
        if bracket == ')' and bracket_stack[-1] != '(':
            _quit()
        if bracket == ']' and bracket_stack[-1] != '[':
            _quit()
        else:
            bracket_stack.pop()
            result += tmp[depth]
            tmp[depth] = 0
            result *= number_stack.pop()
            depth -= 1

if bracket_stack:
    _quit()
else:
    print(result + tmp[0])
