"""
1초 늘리는 방식을 사용하지 않을 때,

<해야할 일>
1. 데이터 가공하기. 시간을 알아보기 쉽도록 변환할 필요가 있음. 모두 초로 변환
2. 각 요청들의 (시작시간 or 끝시간 + 1초)가 기준이 되어서 판별하게 됨.
3. 조건 1) 범위 안에 시작시간이 들어오는 경우
   조건 2) 범위 안에 끝시간이 들어오는 경우
           범위 안에 시작시간, 끝시간이 모두 들어오는 경우는 위 2개 조건에서 걸러짐
   조건 3) 시작시간, 끝시간 사이에 범위가 들어오는 경우

<주의할 점>
1. 0.000초 단위는 100단위로 변하는데, 시분초는 60단위로 움직임
2. 범위시간의 시작시간 또는 끝시간이 완전히 같아버리는 조건도 포함되야 함
   1초는 0.999초를 더하는것으로 보면 편함
"""


def line2time(line):  # 데이터 가공
    # 끝나는 시간
    tmp = line.split()
    end_time = tmp[1].split(':')
    end_time = round(int(end_time[0]) * 3600 + int(end_time[1]) * 60 + float(end_time[2]), 3)

    # 걸린시간
    duration = float(tmp[2][:-1])

    # 시작시간
    if end_time:
        start_time = round(end_time - (duration - 0.001), 3)
    else:
        start_time = 0.0

    return [start_time, end_time]


def check(index_time, timelines):
    global answer

    count = 0
    for start_time, end_time in timelines:

        # 범위안에 시작시간이 들어오는 경우
        if index_time <= start_time <= round(index_time + 0.999, 3):
            count += 1

        # 범위안에 끝시간이 들어오는 경우
        elif index_time <= end_time <= round(index_time + 0.999, 3):
            count += 1

        # 시작시간, 끝시간 사이에 범위가 들어오는 경우
        elif start_time <= index_time and round(index_time + 0.999, 3) <= end_time:
            count += 1

    return count


def solution(lines):
    if len(lines) == 1:
        return 1
    else:
        # 데이터 가공하기
        timelines = []
        for line in lines:
            timelines.append(line2time(line))
        print(timelines)

        answer = 0
        for timeline in timelines:
            for time in timeline:
                count = check(time, timelines)
                if answer < count:
                    answer = count
        return answer
