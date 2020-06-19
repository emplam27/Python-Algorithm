# 새로운 연산을 계산할 건데..
# 좌표 값과 해당 좌표에 매칭되는 값이 필요
# 이차원 배열 만들어서 해당 좌표에 매칭되는 값을 저장
T = int(input())
for t in range(1,T+1):
    numbers = [[0]*300 for _ in range(300)]
    # 초기화된 배열 문제에서 주어진 순서로 순회하면서
    #  숫자 채우기
    count = 1   # 1부터 시작
    for i in range(1,300):
        y = i   # y 의 시작 위치는 i 와 일치
        x = 1   # x는 항상 1부터 시작
        for j in range(1,i+1):    # i번 만큼 반복
            # y는 1씩 감소, x는 1씩 증가
            numbers[y][x] = count
            count += 1
            y -= 1
            x += 1
    p, q = map(int,input().split())
    # p 값을 가지는 좌표 얻어야 함
    # q 값을 가지는 좌표
    # x, y 를 각각 더해서, 새로운 좌표를 얻고
    # 해당 좌표의 value를 얻어오면 됨
    # 좌표 얻어오는 것 : number 배열 순회하면서 검색
    positionP = (0,0)
    positionQ = (0,0)
    for i in range(1,300):  # 배열 순회하면서 좌표 얻어오기
        for j in range(1, 300):
            if numbers[i][j] == p:
                positionP =(i,j)
            if numbers[i][j] == q:
                positionQ = (i, j)
    new_point = (positionP[0] + positionQ[0], positionP[1] + positionQ[1])
    # 새로운 좌표를 얻었으니, 해당 좌표의 값 가져오기
    result = numbers[new_point[0]][new_point[1]]
    print("#%d" % t, result)
