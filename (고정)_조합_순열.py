# 조합
def combinations(arr,r):
    for i in range(len(arr)):  # 함수에서 지금할 일
        if r == 1:  # 종료조건

            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:], r-1):  # 다음에 할 일
                yield [arr[i]] + next


# 아래는 함수를 실행하기 위한 사용법입니다.

for combi in combinations([1,2,3,4,5],2):
    print(combi)


# 중복조합
def combinations_with_replacement(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations_with_replacement(arr[i:], r-1):
                yield [arr[i]] + next


# 중복순열
def product(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in product(arr, r-1):
                yield [arr[i]] + next


# 순열 만들기 : 교환을 통한 순열 만들기
# 조합으로 수를 정해놓고 순열 만드는게 좋을수도..
def perm(idx):
    if idx == N:
        print(arr)
        return

    for i in range(idx, N):
        arr[idx], arr[i] = arr[i], arr[idx]
        perm(idx + 1)
        arr[idx], arr[i] = arr[i], arr[idx]


arr = [1, 2, 3, 4, 5]
N = 5
perm(0)


# 순열 만들기 : 백트레킹을 이용한 순열 만들기
# 시간이 오래걸리는 단점
# 1~8은 0.4초 <= 요정도까지는 쓸만할 듯
# permutation 함수는 0.05초.. 차이가 많이나긴 함
# 1~9까지 약 3초..

def my_permutation(idx, selected, result_list):

    if idx >= len(arr):
        result.append(result_list)
        return

    for i in range(len(arr)):
        if selected[i] == 0:
            selected[i] = 1
            result_list.append(arr[i])
            my_permutation(idx + 1, selected, result_list)
            selected[i] = 0
            result_list.pop()


arr = [1, 2, 3, 4]
result = []
my_permutation(0, [0]*len(arr), [])
print(result)