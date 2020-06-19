import sys

# 표준 입/출력 : 콘솔입출력
sys.stdin = open("input.txt", "r")  # 파일입력

def combination3(idx, selected, count1):

    if idx == 7:
        if count1 == 3:
            sum_num = 0
            for i in range(7):
                if selected[i] == 1:
                    sum_num += arr[i]
            sum_list.append(sum_num)
        return

    if count1 > 3:
        return

    selected[idx] = 1
    count1 += 1
    combination3(idx + 1, selected, count1)
    selected[idx] = 0
    count1 -= 1
    combination3(idx + 1, selected, count1)


T = int(input())
for t in range(1, T + 1):
    arr = list(map(int, input().split()))
    selected = [0] * 7
    sum_list = []

    combination3(0, selected, 0)

    sum_list.sort()
    sum_list2 = []
    j = 0
    for i in sum_list:
        if j < i:
            sum_list2.append(i)
            j = i

    print('#%d' %t, sum_list2[-5])