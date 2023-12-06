from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        cases = list(permutations(nums, len(nums)))
        return [list(permutation) for permutation in cases]
        
        
#         ans = []
#         combination = []
#         def back(combination, nums):
#             if len(combination) == len(nums):
#                 ans.append(combination)
#             else:
#                 for idx, num in enumerate(nums):
                    
#                     back(combination + [num], nums[idx:])
#         back(combination, nums)
#         return ans
                