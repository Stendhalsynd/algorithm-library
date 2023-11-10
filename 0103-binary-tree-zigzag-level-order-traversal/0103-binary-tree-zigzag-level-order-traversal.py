from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 09:20
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return root
        
        nodes = []
        queue = deque([root])
        
        flag = False
        
        while queue:
            temp = deque([])
            
            lenQ = len(queue)
            for _ in range(lenQ):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                if flag:
                    temp.appendleft(node.val)
                else:
                    temp.append(node.val)
            flag = not flag
            nodes.append(list(temp))
        
        return nodes