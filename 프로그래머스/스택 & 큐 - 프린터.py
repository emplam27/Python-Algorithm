def solution(priorities, location):
    priorities = [[priorities[index], index] for index in range(len(priorities))]
    order, order_dict = 1, dict()
    while priorities:
        tmp = priorities.pop(0)
        if not priorities:
            order_dict[tmp[1]] = order
            break
        if max(priorities, key=lambda x: x[0])[0] <= tmp[0]:
            order_dict[tmp[1]] = order
            order += 1
            continue
        priorities.append(tmp)
    return order_dict[location]