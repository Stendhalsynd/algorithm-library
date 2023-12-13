# ~ 08:40
from bisect import bisect_left
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]

        start, end = 0, len(nums) - 1
        mid = 0
        while start < end:
            mid = (start + end) // 2
            if nums[start] < nums[mid - 1] and nums[mid] < nums[end]: # 왼쪽, 오른쪽이 모두 정렬되어 있다
                return nums[mid]
            else:
                if nums[mid] >= nums[end]: # 4 5 6 7 0 1 2 에서 4 5 6 / 7 0 1 2 로 나뉘어 nums[mid] 가 7 이었을 때
                    start += 1
                elif nums[start] >= nums[mid - 1]: # 4 5 6 7 0 1 2 에서 4 5 6 7 0 / 1 2 로 나뉘어 nums[mid] 가 1 이었을 때
                    end -= 1

        return nums[end]