# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# ~08:40
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.stack = []
        self.result = True
        
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            if self.stack and self.stack[-1] >= root.val:
                self.result = False
                return
            self.stack.append(root.val)
            inorder(root.right)
        inorder(root)
        return self.result