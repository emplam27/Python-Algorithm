import sys

# 표준 입/출력 : 콘솔입출력
sys.stdin = open("input.txt", "r")  # 파일입력

T = int(input())
for t in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())

    h_sum = h1 + h2
    m_sum = m1 + m2
    if m_sum > 60:
        m_sum -= 60
        h_sum += 1
    if h_sum > 12:
        h_sum -= 12

    print('#%d' % t, h_sum, m_sum)
