def solution(m, music_infos):
    def time2minute(time):
        time = list(map(int, time.split(':')))
        return time[0] * 60 + time[1]

    def makelist(string):
        index = 0
        result = []
        while index < len(string):
            if index != len(string) - 1 and string[index + 1] == "#":
                result.append(string[index:index + 2])
                index += 2
            else:
                result.append(string[index])
                index += 1
        return result

    m = makelist(m)

    result = "(None)"
    max_time = 0
    # [재생시간, 제목, 재생시간만큼 반복된 음계]로 정리
    for index, info in enumerate(music_infos):
        info = info.split(',')
        time = time2minute(info[1]) - time2minute(info[0])
        info[3] = makelist(info[3])
        music_infos[index] = [time, info[2], info[3] * (time // len(info[3])) + info[3][:time % len(info[3])]]

    # 포함하는지 확인
    for music in music_infos:
        for index, note in enumerate(music[2]):
            if note == m[0]:
                for i in range(1, len(m)):
                    if index + i >= len(music[2]) or not music[2][index + i] == m[i]:
                        break
                else:  # 포함하면
                    if music[0] > max_time:  # 최대 재생 시간인지 확인
                        max_time = music[0]
                        result = music[1]
                        break

    return result