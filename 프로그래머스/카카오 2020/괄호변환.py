def solution(p):

    if p == '':
        return ''

    count_bracket = [0, 0]
    for bracket in p:
        if bracket == '(':
            count_bracket[0] += 1
        else:
            count_bracket[1] += 1
        if count_bracket[0] == count_bracket[1]:
            break
    u, v = p[:count_bracket[0] * 2], p[count_bracket[0] * 2:]

    stack, is_correct = [], True
    for u_bracket in u:
        if u_bracket == '(':
            stack.append('(')
        else:
            if not len(stack):
                is_correct = False
                break
            if stack[-1] == '(':
                stack.pop()
            else:
                is_correct = False
                break

    if is_correct:
        return u + solution(v)
    else:
        tmp = []
        for val in u[1:-1]:
            if val == '(':
                tmp.append(')')
            else:
                tmp.append('(')
        return '(' + solution(v) + ')' + ''.join(tmp)


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
