def solution(records):
    results = []
    user_info = dict()

    for record in records:
        record = record.split()

        if record[0] == 'Enter':
            user_info[record[1]] = record[2]
            results.append([record[1], 0])

        elif record[0] == 'Leave':
            results.append([record[1], 1])

        else:
            user_info[record[1]] = record[2]

    for index, result in enumerate(results):
        if result[1] == 0:
            results[index] = "{}님이 들어왔습니다.".format(user_info[result[0]])
        else:
            results[index] = "{}님이 나갔습니다.".format(user_info[result[0]])

    return results
