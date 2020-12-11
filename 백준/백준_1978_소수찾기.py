import sys

sys.stdin = open('input.txt', 'r')

N = int(input())
nums = list(map(int, input().split()))

prime_number = [0] * 2 + [1] * 999
for index in range(len(prime_number)):
    if prime_number[index] == 1:
        tmp_index = index * 2
        while tmp_index <= 1000:
            prime_number[tmp_index] = 0
            tmp_index += index

result = 0
for num in nums:
    if prime_number[num] == 1:
        result += 1
print(result)
