def quick_sort(arr, left, right):

    # left, right가 교차되버리면 종료
    if left > right:
        return

    # 피벗 찾기
    pivot = find_pivot(arr, left, right)

    # 좌, 우 분할정렬
    quick_sort(arr, left, pivot - 1)

    quick_sort(arr, pivot + 1, right)


def find_pivot(arr, left, right):
    start, end = left, right
    pivot = arr[left]

    # start < end일 동안만 반목
    while start <= end:

        # start가 pivot보다 큰 값을 찾을 때 까지 +1
        while start <= end and arr[start] <= pivot:
            start += 1

        # end가 pivot보다 작은 값을 찾을 때 까지 -1
        while start <= end and arr[end] >= pivot:
            end -= 1

        # start < end 이면 위치교환
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]

    # start > end가 되면 피벗을 기준으로 정렬이 완료되었다는 의미
    # 이때 start는 pivot보다 큰 수를, end는 pivot보다 작은수를 가르키고 있음
    arr[end], arr[left] = arr[left], arr[end]

    return end  # pivot 위치


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        quick_sort(nums, 0, len(nums) - 1)
        return nums

