def time2min(str1):
    return int(str1.split(':')[0]) * 60 + int(str1.split(':')[1])


def min2time(num):
    return '{:02}:{:02}'.format(num // 60, num % 60)


def crewtime(timetable):
    return [time2min(time) for time in timetable]


def shuttletime(n, t):
    shuttle = [0] * n
    for i in range(n):
        shuttle[i] = 540 + i * t
    return shuttle

def check(time, crew, shuttle, m):
    arr = [0] + [i for i in crew]

    # 콘의 현재위치와 배열 만들기
    current = 0
    for i in range(len(arr)):
        if arr[i] > time:
            arr.insert(i, time)
            current = i
            break
    else:
        arr.append(time)
        current = len(arr) - 1

    # 버스시간에 맞춰서 탈 수 있는 경우 구하기
    visit = [1] + [0] * (len(arr) - 1)
    visit_num = 0
    for bus in shuttle:
        tmp = 0
        while tmp < m:
            for j in range(visit_num, len(arr)):
                if arr[j] <= bus and visit[j] == 0:
                    visit[j] = 1
                    visit_num += 1
                    tmp += 1
                    break
            else:
                break
    if visit_num >= current:
        return time




def solution(n, t, m, timetable):

    crew = sorted(crewtime(timetable))
    shuttle = shuttletime(n, t)

    # 검사해야하는 시간대
    # 크루들보다 1분 일찍 왔을 때,
    # 크루들과 같은 시간에 왔을 때, 이것은 고려하지 않아도 괜찮음.
    # 셔틀과 같은 시간에 왔을 때,
    max_result = 0
    for i in set(crew):
        # 크루들보다 1분 일찍 왔을 때
        tmp = check(i - 1, crew, shuttle, m)
        if tmp != None and tmp > max_result:
            max_result = tmp
        # # 크루들과 같은 시간에 왔을 때
        # tmp = check(i, crew, shuttle, m)
        # if tmp != None and tmp > max_result:
        #     max_result = tmp
    for i in shuttle:
        # 셔틀과 같은 시간에 왔을 때
        tmp = check(i, crew, shuttle, m)
        if tmp != None and tmp > max_result:
            max_result = tmp


    return min2time(max_result)