import copy

def solution(user_ids, banned_ids):
    
    def check_id(order, banned_id):
        for user_id in len_user_id[len(banned_id)]:
            for index, char in enumerate(user_id):
                if banned_id[index] != '*' and banned_id[index] != char:
                    break
            else:
                banned_id_candidate[order].append(user_id)
        return
        
        
    def combination(index, max_index):
        nonlocal result
        
        if index >= max_index:
            tmp_selected = copy.deepcopy(selected)
            if tmp_selected not in result_list:
                result_list.append(tmp_selected)

                result += 1
            return
        
        for cand_id in banned_id_candidate[index]:
            if cand_id not in selected:
                selected.add(cand_id)
                combination(index + 1, max_index)
                selected.remove(cand_id)
    
    
    # user_id를 길이별로 묶기
    len_user_id = [[] for _ in range(9)]
    for user_id in user_ids:
        len_user_id[len(user_id)].append(user_id)
    
    # 각 banned_id 마다 해당될 수 있는 user_id를 걸러내기
    banned_id_candidate = [[] for _ in range(len(banned_ids))]
    for order, banned_id in enumerate(banned_ids):
        if banned_id == '*' * len(banned_id):
            banned_id_candidate[order] = len_user_id[len(banned_id)]
        else:
            check_id(order, banned_id)

    
    # 조합 구하기
    selected = set()
    result_list = list()
    result = 0
    combination(0, len(banned_ids))
    
    return result