import heapq


def solution(scoville, K):
    answer = 0
    scoville.sort()

    while len(scoville) > 1:
        tmp1 = heapq.heappop(scoville)
        if tmp1 >= K:
            return answer
        tmp2 = heapq.heappop(scoville)
        heapq.heappush(scoville, tmp1 + (tmp2 * 2))
        answer += 1
    if len(scoville) == 1 and scoville[0] >= K:
        return answer
    else:
        return -1