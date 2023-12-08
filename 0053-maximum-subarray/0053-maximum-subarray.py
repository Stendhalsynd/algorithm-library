# 08:50
# array, divide and conquer, dp
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_val = max(nums) 
        if max_val < 0:
            return max_val
        max_sub = 0

        for val in nums:
            max_sub = max(max_sub + val, val)
            if max_val < max_sub:
                max_val = max_sub

        return max_val