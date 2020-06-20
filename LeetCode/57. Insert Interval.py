class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 새로운 interval이 어느 영역들과 만나는지 봐야함
        # 몇개가 겹칠지 모르므로, 매번 겹치는지 확인해줘야함
        # interval 범위 밖의 요소는 그냥 더해줌

        result = []
        for index, interval in enumerate(intervals):

            # interval 보다 작을 때
            if interval[1] < newInterval[0]:
                result.append(interval)

            # interval 보다 클 때
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                result.extend(intervals[index:])
                return result

            # interval과 겹칠 때
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])

            print(newInterval)

        # newInterval이 마지막이면
        result.append(newInterval)
        return result