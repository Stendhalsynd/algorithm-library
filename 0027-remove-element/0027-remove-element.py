# 08:35
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while nums.count(val) > 0:
            nums.remove(val)
        return len(nums)

        # idx = 0
        # count = 0
        # for num in nums:
        #     if num != val:
        #         nums[idx] = num
        #         idx += 1
        #         count += 1
        # return count