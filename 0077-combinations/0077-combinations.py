from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
#         total = [val for val in range(1, n + 1)]
        
#         cases = list(combinations(total, k))
#         answer = [list(combination) for combination in cases]
        
#         return answer

        ans = []
        nums = [val for val in range(1, n + 1)]
        combination = []
        def back(combination, nums):
            if len(combination) == k:
                ans.append(combination)
            else:
                for idx, num in enumerate(nums):
                    if not combination:
                        back([num], nums[idx:])
                    elif combination and combination[-1] < num:
                        back(combination + [num], nums[idx:])
        back(combination, nums)
        return ans
                