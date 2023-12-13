# 09:15
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        que = []
        for val in nums:
            heapq.heappush(que, val)
        group = heapq.nlargest(k, que)
        return group[-1]