import sys

sys.stdin = open('input.txt', 'r')


string = input()

# Suffix Array O(N)
suffix_array = sorted([[string[index:], index + 1] for index in range(len(string))], key=lambda x: x[0])

# Suffix Array O(NlogN
print(suffix_array)

# Longest Common Prefix, 최장 공통 접두사
# LCP =