"""
<해야할 일>
[가로좌표, 세로좌표, 0:기둥/1:보, 0:삭제/1:설치]
2차원 배열 안에 기둥과 보를 나타낼 수 있어야 함. 혹은 두개의 배열안에 나눠 나열할 수 있어야 함
기둥: 바닥의 좌표를 기준으로 2차원 배열에 표현
보: 왼쪽 좌표를 기준으로 2차원 배열에 표현
"""


def solution(n, build_frame):

    pillars = [[0] * (n + 1) for _ in range(n + 1)]
    beams = [[0] * (n + 1) for _ in range(n + 1)]

    for c, r, a, b in build_frame:

        if a == 0:  # '기둥'이면서
            # 설치일 때,
                # 아래 기둥이 있으면 설치
                # 아래 보가 있으면 설치
            # 삭제일 때,
                # 기둥 위에 기둥이 있으면 무시
                # 기둥 위에 보가 하나이면 무시
                # 기둥 위에 보가 2개인데, 하나가 다른곳과 연결이 안된 곳이라면 무시



       else:  # '보'이면서
            # 설치일 때,
                # 좌, 우에 기둥이 하나만 있으면 설치, 양쪽다 연결이면 설치 x
                # 좌, 우에 모두 보가 있으면 설치
            # 삭제일 때,
                #

    return