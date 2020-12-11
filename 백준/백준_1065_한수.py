import sys

sys.stdin = open('input.txt', 'r')

'''
연속된 두자리의 수가 등차수열
각 자리수를 뒤에서부터 구하며 차이를 구한다. 차이값이 끝까지 같다면 한수 
'''

N = int(input())
if N < 100:
    print(N)
else:
    result = 99
    for num in range(100, N + 1):
        num = list(map(int, str(num)))
        if num[1] - num[0] == num[2] - num[1]:
            result += 1
    print(result)

