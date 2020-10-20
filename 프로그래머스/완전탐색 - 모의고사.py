def solution(answers):
    sol_1 = [1, 2, 3, 4, 5]
    sol_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    sol_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    results, result_1, result_2, result_3 = [[] for _ in range(len(answers) + 1)], 0, 0, 0
    index_1, index_2, index_3 = 0, 0, 0
    for answer in answers:
        if sol_1[index_1] == answer: result_1 += 1
        if sol_2[index_2] == answer: result_2 += 1
        if sol_3[index_3] == answer: result_3 += 1
        index_1, index_2, index_3 = index_1 + 1, index_2 + 1, index_3 + 1
        if index_1 == len(sol_1): index_1 = 0
        if index_2 == len(sol_2): index_2 = 0
        if index_3 == len(sol_3): index_3 = 0
    results[result_1].append(1)
    results[result_2].append(2)
    results[result_3].append(3)
    for result in results[::-1]:
        if result: return result
