
arr = list(map(int, input().split()))

for i in range(max(arr), 0, -1):
    list01 = []
    for j in range(len(arr)):
        if arr[j] >= i:
            list01.append(1)
        elif arr[j] < i:
            list01.append(0)

    list2 = []
    sum1 = 0
    for k in range(len(list01)):
        if list01[k] == 1:
            sum1 += 1
        if list01[k] == 0:
            list2.append(sum1)
            sum1 = 0
    list2.append(sum1)

    max_size = 0
    for l in range(len(list2)):
        if list2[l] * i > max_size:
            max_size = list2[l] * i

print(max_size)
