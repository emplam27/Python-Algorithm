import sys

sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline

'''
LIS(Longest Increasing Subsequence, 최장증가수열) 알고리즘
시간복잡도: O(nlogn)

수열을 순회하면서 작은 숫자부터 차례대로 검사한다.
1. 해당 숫자가 stack의 가장 마지막 요소보다 크다면 스택에 넣어준다.
2. 해당 숫자가 stack의 가장 마지막 요소보다 작다면 스택안에서 이분탐색을 실행한다.
    본인보다 작은 값 중 가장 큰 값을 찾아 그 다음값을 해당 숫자로 교체한다. 
    해당 숫자가 교체되어도 스택 안 숫자들의 정렬은 깨지지 않는다.  
'''

N = int(read().rstrip())
numbers = list(map(int, read().rstrip().split()))

LIS = [numbers[0]]
for number in numbers[1:]:
    if LIS[-1] < number:
        LIS.append(number)
    else:
        start, end = 0, len(LIS)
        while start <= end:
            mid = (start + end) // 2
            if LIS[mid] >= number:
                end = mid - 1
            else:
                start = mid + 1
        LIS[start] = number
print(len(LIS))

