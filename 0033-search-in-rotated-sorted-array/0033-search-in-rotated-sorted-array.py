from bisect import bisect_left
from collections import deque
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # return nums.index(target) if nums.count(target) > 0 else -1

        if len(nums) == 1 and nums[0] != target:
            return -1

        que = deque(nums)
        count = 0
        while que[0] > que[-1]:
            que.rotate(-1)
            count += 1
        point = bisect_left(list(que), target)

        if point >= len(nums):
            return -1

        return (point + count) % len(nums) if que[point] == target else -1