T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 모든 숫자 경우의수 가져오기
    max_num = -1

    for i in range(N-1):
        for j in range(i + 1, N):
            result = 1
            num = arr[i] * arr[j]

            # 문자열을 이용하지 않고 구해보자.
            # 숫자를 뒤쪽에서 부터 나누면 각자리 숫자를 쉽게 구할 수 있다.
            prev = 10   # 비교를 위해 만든 변수
            is_asc = True
            origin_num = 0
            while num > 0:  # 나눌 숫자가 없어질때 까지 반복한다.
                target = num % 10   # 나머지 구하기
                num = num // 10       # 몫 구하기
                # 만약에 이전 숫자보다 크다면, 단조증가수가 아님
                if prev < target:
                    # 단조증가수가 아님
                    is_asc = False
                    break
                prev = target

            if is_asc:
                if origin_num > max_num:
                    max_num = origin_num

    print('#%d' % t, max_num)
