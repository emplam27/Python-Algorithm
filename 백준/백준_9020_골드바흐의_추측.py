import sys

sys.stdin = open('input.txt', 'r')

N = int(input())
for _ in range(N):
    even_num = int(input())

    # '에라토스테네스의 체' 사용하여 소수 구하기
    prime_number = [0] * 2 + [1] * 9999
    for index in range(len(prime_number)):
        if prime_number[index] == 1:
            tmp_index = index * 2
            while tmp_index <= 10000:
                prime_number[tmp_index] = 0
                tmp_index += index
    prime_numbers = [index for index, value in enumerate(prime_number) if value == 1]

    # 소수간의 합 구하기
    result, min_dis = [], 2**31
    for first_prime_index in range(len(prime_numbers)):
        # 한 소수가 구하고자하는 짝수의 반을 넘어가면 멈추기
        first_prime_number = prime_numbers[first_prime_index]
        if first_prime_number > even_num / 2:
            break

        # 나머지 소수가 존재하지 않으면 넘어가기
        target_prime_number = even_num - first_prime_number
        if target_prime_number not in prime_numbers:
            continue
        else:
            result = [str(first_prime_number), str(target_prime_number)]
    print(' '.join(result))
