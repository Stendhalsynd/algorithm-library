from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        total = [val for val in range(1, n + 1)]
        
        cases = list(combinations(total, k))
        answer = [list(combination) for combination in cases]
        
        return answer