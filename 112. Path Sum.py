# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Given the root of a binary tree 
and an integer targetSum, 
return true if the tree has a root-to-leaf path 
that adding up all the values along the path equals targetSum.
'''
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ## DFS
        if root is None:
            return False
        if root.right is None and root.left is None and root.val == targetSum:
            return True
        else:
            return self.hasPathSum(root.right, targetSum-root.val) or self.hasPathSum(root.left, targetSum-root.val)