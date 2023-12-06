# ~ 08:50
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []
        combination = []
        
        def back(combination, nums):
            
            if sum(combination) == target:
                ans.append(combination)
                
            else:
                for idx, num in enumerate(nums):
                    
                    if not combination:
                        back([num], nums[idx:])
                             
                    elif combination and sum(combination) < target:
                        back(combination + [num], nums[idx:])
                             
        back(combination, candidates)        
        return ans