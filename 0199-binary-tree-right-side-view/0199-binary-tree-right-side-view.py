from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        
        def dfs(node = root, level = 1):
            if not node:
                return
            if len(answer) < level:
                answer.append(node.val)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
            
        dfs()
        
        return answer
#         if root is None:
#             return
        
#         queue = deque([])
#         right_side = []
#         last_node = 0
        
#         queue.append(root)
        
#         queue.append(None)
        
#         # BFS
#         while len(queue) > 0:
#             node = queue.popleft()
#             if node is None:
#                 right_side.append(last_node)
#                 queue.append(None)
                
#                 if queue[0] is None:
#                     break
#                 else:
#                     continue
            
#             last_node = node.val
            
#             if node.left is not None:
#                 queue.append(node.left)
                
#             if node.right is not None:
#                 queue.append(node.right)
        return right_side