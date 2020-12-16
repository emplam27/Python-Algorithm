import sys

sys.stdin = open('input.txt', 'r')


# 힙정렬 구현
# 1. 힙이 아닌 배열을 힙으로 만들어주기
# 2. 힙의 루트(가장 큰 수)를 꺼내서 배열의 가장 마지막에 넣어주기
# 3. 남은 배열을 다시 힙으로 구성하기
# 4, 2번, 3번 반복하여 큰수에서부터 정렬하기

def heap_sort(nums):

    def make_heap(array, index, heap_size):
        parent = index
        left_child = 2 * parent + 1
        right_child = 2 * parent + 2

        if left_child < heap_size and array[left_child] > array[parent]:
            parent = left_child
        if right_child < heap_size and array[right_child] > array[parent]:
            parent = right_child
        if parent != index:
            array[parent], array[index] = array[index], array[parent]
            make_heap(array, parent, heap_size)

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
