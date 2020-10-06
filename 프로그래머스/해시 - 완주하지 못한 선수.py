def solution(participant, completion):
    dict_completion = dict()
    for comp in completion:
        if dict_completion.get(comp) == None:
            dict_completion[comp] = 1
        else:
            dict_completion[comp] += 1

    for part in participant:
        if dict_completion.get(part) == None or dict_completion.get(part) == 0:
            return part
        dict_completion[part] -= 1