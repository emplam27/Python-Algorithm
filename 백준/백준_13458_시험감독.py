import sys

sys.stdin = open("input.txt", "r")

N = int(input())
rooms = list(map(int, input().split()))
B, C = map(int, input().split())

rooms = [room - B for room in rooms]
result = len(rooms)
for room in rooms:
    if room > 0:
        if room % C:
            result += room // C + 1
        else:
            result += room // C
print(result)
