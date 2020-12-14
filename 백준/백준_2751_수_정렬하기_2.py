import sys

sys.stdin = open('input.txt', 'r')


# 힙정렬 구현
# 1. 힙이 아닌 배열을 힙으로 만들어주기
# 2. 힙의 루트(가장 큰 수)를 꺼내서 배열의 가장 마지막에 넣어주기
# 3. 남은 배열을 다시 힙으로 구성하기
# 4, 2번, 3번 반복하여 큰수에서부터 정렬하기

def heap_sort(nums):

    def make_heap(array, index, heap_size):
        root_index = index
        left_index = 2 * root_index + 1
        right_index = 2 * root_index + 2

        if left_index < heap_size and array[left_index] > array[root_index]:
            root_index = left_index
        if right_index < heap_size and array[right_index] > array[root_index]:
            root_index = right_index
        if root_index != index:
            array[root_index], array[index] = array[index], array[root_index]
            make_heap(array, root_index, heap_size)

    for i in range((N - 1) // 2, -1, -1):
        make_heap(nums, i, N)

    for i in range(N - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        make_heap(nums, 0, i)


r = sys.stdin.readline
N, nums = int(r()), []
for _ in range(N):
    nums.append(int(r()))

heap_sort(nums)

for num in nums:
    print(num)
