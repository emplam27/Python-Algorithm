'''
hashing을 이용한 문자열 탐색 알고리즘
비교 문자열의 hash값과 원본 문자열의 hash값을 비교하여 같은 hash값이 나오면 비교

다음 문자열의 hash값을 찾을 때
Rabin fingerprint 해쉬함수를 사용하여 O(1)로 다음 hash값을 찾을 수 있음
'''


def hash_value(nums):
    # Rabin fingerprint 해시함수
    value = 0
    for index, num in enumerate(nums[::-1]):
        value += num * 2 ** index

    return value


std_origin_string = "ABCDABDSASBAABCCABACBACABCBACBSDASCACSBCABACACBABCABC"
com_origin_string = "ABC"
std_string, com_string = list(map(ord, std_origin_string)), list(map(ord, com_origin_string))

# 비교 문자열의 hash값 구하기
hash_com = hash_value(com_string)

# 기준 문자열의 처음 hash값을 구하고, 이후에는 O(1)로 계산하기
hash_std = hash_value(std_string[0:len(com_string)])
std_start = 0
while True:
    # 만일 hash값이 동일하다면 문자열까지 동일한지 검사
    if hash_std == hash_com:
        if std_string[std_start: std_start + len(com_string)] == com_string:
            print(std_start)
    # O(1)로 해쉬값 계산하기
    try:
        hash_std = (hash_std - (std_string[std_start] * (2 ** (len(com_string) - 1)))) * 2 + (
        std_string[std_start + len(com_string)])
        std_start += 1
    except:
        break
