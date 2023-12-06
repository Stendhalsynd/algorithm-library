from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # cases = list(permutations(nums, len(nums)))
        # return [list(permutation) for permutation in cases]
        
        ans = []
        permutation = []
        def back(permutation):
            if len(permutation) == len(nums):
                ans.append(permutation)
            else:
                for num in nums:
                    if not permutation:
                        back([num])
                    elif permutation and num not in permutation:
                        back(permutation + [num])
        back(permutation)
        return ans
                