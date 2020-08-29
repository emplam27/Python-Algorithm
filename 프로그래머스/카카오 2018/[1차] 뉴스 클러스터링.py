import math

def solution(str1, str2):
    answer = 0
    if len(str1) == 0 and len(str2) == 0:
        return 65536

    str1 = str1.lower()
    str2 = str2.lower()

    str1_sub, str2_sub = dict(), dict()
    for i in range(len(str1) - 1):
        if 97 <= ord(str1[i]) <= 122 and 97 <= ord(str1[i + 1]) <= 122:
            if str1_sub.get(str1[i:i + 2]):
                str1_sub[str1[i:i + 2]] += 1
            else:
                str1_sub[str1[i:i + 2]] = 1
    for i in range(len(str2) - 1):
        if 97 <= ord(str2[i]) <= 122 and 97 <= ord(str2[i + 1]) <= 122:
            if str2_sub.get(str2[i:i + 2]):
                str2_sub[str2[i:i + 2]] += 1
            else:
                str2_sub[str2[i:i + 2]] = 1

    # 교집합, 합집합
    intersection, union = 0, 0
    for key in str1_sub.keys():
        if str2_sub.get(key):
            intersection += min(str1_sub[key], str2_sub[key])
            union += max(str1_sub[key], str2_sub[key])
        else:
            union += str1_sub[key]
    for key in str2_sub.keys():
        if not str1_sub.get(key):
            union += str2_sub[key]

    if union == 0:
        return 65536

    return math.floor(65536 * (intersection / union))

print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))