# import sys

# sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T + 1):
    arr = list(map(int, input().split()))

    num_list = []
    for i in range(10):
        num = arr[i]
        sum_num = 0
        while num > 0:
            num1 = num % 10
            num2 = num // 10
            sum_num += num1
            num = num2
        num_list.append(sum_num)

    print('#%d' %t, max(num_list), min(num_list))
