"""
LRU(Least Recently Used) 알고리즘
사용된지 가장 오랫동안 참조되지 않은 페이지를 교체하는 알고리즘
이외 선입선출의 FIFO알고리즘, 가장 적은 횟수를 참조한 페이지를 교체하는 LFU알고리즘 등이 존재

"""

from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque()

    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower()
        if city not in cache:
            answer += 5
            if len(cache) >= cacheSize and len(cache) != 0:
                cache.popleft()
        else:
            cache.remove(city)
            answer += 1
        cache.append(city)

    return answer
