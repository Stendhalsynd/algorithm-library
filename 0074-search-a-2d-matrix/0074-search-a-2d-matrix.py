# from bisect import bisect_left
from collections import deque
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        que = deque(sum(matrix, []))
        return que.count(target) > 0