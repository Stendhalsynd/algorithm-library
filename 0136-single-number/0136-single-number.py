# ~ 08:55
# from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # counter = Counter(nums)
        
        # for key, val, in counter.items():
        #     if val == 1:
        #         return key

        a = 0
        for i in nums:
            a ^= i
        return a