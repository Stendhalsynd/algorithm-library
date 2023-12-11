from bisect import bisect_left
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row in matrix:
            if bisect_left(row, target) < len(row) and row.count(target) > 0:
                return True
        return False