for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    new_arr = []
    for i in range(1, M + 1):
        new_arr.append([arr[i-1], i])

    oven = [[0, 0] for _ in range(N)]
    while len(oven) > 0:

        oven[0][0] = oven[0][0] // 2

        if oven[0][0] == 0:
            result = oven.pop(0)
            if len(new_arr) > 0:
                tmp = new_arr.pop(0)
                oven.append(tmp)
                continue
            else:
                continue

        else:
            tmp = oven.pop(0)
            oven.append(tmp)
            continue


    print('#%d' %t, result[1])
