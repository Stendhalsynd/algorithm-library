from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 08:50
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = []
        queue = deque([root])
        
        if root is None:
            return nodes
        
        queue.append(None)
        temp = []
        
        while len(queue) > 0:
            node = queue.popleft()
            if node is None:
                nodes.append(temp)
                queue.append(None)
                temp = []
                
                if queue[0] is None:
                    break
                else:
                    continue
            
            temp.append(node.val)
            
            if node.left is not None:
                queue.append(node.left)
                
            if node.right is not None:
                queue.append(node.right)
                
        return nodes
                