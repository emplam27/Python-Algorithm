def solution(dart_result):
    answer = 0

    index, order = 0, -1
    points = [0] * 3
    while index < len(dart_result):
        if dart_result[index].isnumeric():
            order += 1
            if dart_result[index + 1] == '0':
                points[order] = 10
                index += 1
            else:
                points[order] = int(dart_result[index])
        elif dart_result[index].isalpha():
            if dart_result[index] == "D":
                points[order] **= 2
            elif dart_result[index] == "T":
                points[order] **= 3
        else:
            if dart_result[index] == '*':
                if order == 0:
                    points[order] *= 2
                else:
                    points[order] *= 2
                    points[order - 1] *= 2
            else:
                points[order] *= -1
        index += 1

    for point in points:
        answer += point

    return answer