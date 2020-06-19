T = int(input())
for t in range(1, T + 1):
    arr = list(map(int, input().split()))

    arr.sort()

    sum_num = 0
    for i in arr[1:9]:
        sum_num += i

    print('#%d' % t, round(sum_num / 8))