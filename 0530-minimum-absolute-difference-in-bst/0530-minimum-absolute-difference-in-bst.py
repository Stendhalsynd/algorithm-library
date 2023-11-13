# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        minDiff = 100000
        isInitial = True
        beforeVal = 0
        def inorder(root):
            nonlocal minDiff, isInitial, beforeVal
            if root is None:
                return
            inorder(root.left)
            if isInitial:
                isInitial = False
                beforeVal = root.val
            else:
                if root.val - beforeVal < minDiff:
                    minDiff = root.val - beforeVal
                beforeVal = root.val
            inorder(root.right)
        inorder(root)
        return minDiff
                
                