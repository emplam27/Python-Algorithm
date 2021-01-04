import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

'''
한개의 성적을 기준으로 정렬한다. 
이후 앞에서 부터 순회하면서 앞에 본인보다 높은 등수가 있다면 떨어진다.
높은 등수가 없다면 결과값을 하나 올리고 가장 높은 등수를 갱신한다. 
'''

T = int(read().rstrip())
for _ in range(T):
    N = int(read().rstrip())
    candidates = [0] * (N + 1)
    for _ in range(N):
        a, b = map(int, read().rstrip().split())
        candidates[a] = b

    min_rank, result = 100001, 0
    for index in range(1, N + 1):
        if min_rank > candidates[index]:
            min_rank = candidates[index]
            result += 1
    print(result)

