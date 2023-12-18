# ~ 08:55
# from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return nums[0]
        
        # counter = Counter(nums)
        
        # for key, val, in counter.items():
        #     if val == 1:
        #         return key

        a = 0
        for i in nums:
            a ^= i # 0 XOR 4 XOR 1 XOR 2 XOR 1 XOR 2 = 4
        return a