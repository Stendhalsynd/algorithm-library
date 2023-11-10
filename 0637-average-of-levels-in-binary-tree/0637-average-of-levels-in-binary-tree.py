from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return
        
        q = deque([])
        averages = []

        q.append(root)
        nodes_count_per_level = 0
        sum_per_level = 0

        q.append(None)

        while len(q) > 0:
            node = q.popleft()
            if node is None:
                averages.append(sum_per_level / nodes_count_per_level)
                sum_per_level = 0
                nodes_count_per_level = 0
                q.append(None)
                
                if q[0] is None:
                    break
                else:
                    continue
            
            sum_per_level += node.val
            nodes_count_per_level += 1

            if node.left is not None:
                q.append(node.left)

            if node.right is not None:
                q.append(node.right)
        return averages


