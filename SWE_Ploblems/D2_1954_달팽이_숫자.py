T = int(input())

for t in range(1, T + 1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]

    # 우 하 좌 상
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    r, c = 0, 0
    direct = 0
    i = 1
    result = ''

    while i < n ** 2 + 1:

        # 남은자리가 없다면 반복문을 종료한다.
        if arr[r][c] != 0:
            break

        # 0을 만날때마다 값을 집어넣어준다.
        arr[r][c] = i
        i += 1
        tr = r + dy[direct]
        tc = c + dx[direct]

        # 벽을 만나면 우 하 좌 상으로 꺾어준다.
        if tr < 0 or tr >= len(arr) or tc < 0 or tc >= len(arr) or arr[tr][tc] != 0:
            direct = (direct + 1) % 4
            tr = r + dy[direct]
            tc = c + dx[direct]
        r = tr
        c = tc

    for r in range(len(arr)):
        for c in range(len(arr[r])):
            if c % n != n - 1:
                result = result + '%d' % arr[r][c] + ' '
            if c % n == n - 1:
                result = result + '%d' % arr[r][c] + '\n'
    print('#%d' % t)
    print(result[:-1])


