def solution(n, t, m, timetable):
    timetable = [int(i[:2]) * 60 + int(i[3:]) for i in timetable]
    timetable.sort()
    shuttle = [9 * 60 + t * i for i in range(n)]

    for i in shuttle:
        passenger = [p for p in timetable if p <= i]

        if i == shuttle[-1]:
            if len(passenger) >= m:
                answer = passenger[m - 1] - 1
            elif len(passenger) < m:
                answer = i
            else:
                answer = passenger[-1]

        elif len(passenger) < m:
            timetable = timetable[len(passenger):]

        elif len(passenger) >= m:
            timetable = timetable[m:]

    answer = str(divmod(answer, 60)[0]).rjust(2, '0') + ':' + str(divmod(answer, 60)[1]).rjust(2, '0')
    return answer
