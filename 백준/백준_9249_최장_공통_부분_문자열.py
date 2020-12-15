import sys

sys.stdin = open('input.txt', 'r')


def hash_value(nums):
    # Rabin fingerprint 해시함수
    value = 0
    for index, num in enumerate(nums[::-1]):
        value += num * 2 ** index

    return value


def check_matching(length, std_start, com_start):
    if std_string[std_start: std_start + length] == com_string[com_start:com_start + length]:
        return True


A, B = input(), input()

std_origin_string, com_origin_string = [A, B] if len(A) > len(B) else [B, A]
std_string, com_string = list(map(ord, std_origin_string)), list(map(ord, com_origin_string))

for len_com_string in range(len(com_string), 0, -1):
    for com_start in range(0, len(com_string) - len_com_string + 1):
        # 비교 문자열의 hash값 구하기
        hash_com = hash_value(com_string[com_start:com_start + len_com_string])

        # 기준 문자열의 처음 hash값을 구하고, 이후에는 O(1)로 계산하기
        hash_std = hash_value(std_string[0:len_com_string])
        std_start = 0
        while std_start < len(std_string) - len_com_string:
            if hash_std == hash_com:
                if check_matching(len_com_string, std_start, com_start):
                    print(len_com_string)
                    print(com_origin_string[com_start: com_start + len_com_string])
                    exit()
            # O(1)로 해쉬값 계산하기
            hash_std = (hash_std - (std_string[std_start] * (2 ** (len_com_string - 1)))) * 2 + (
            std_string[std_start + len_com_string])
            std_start += 1
