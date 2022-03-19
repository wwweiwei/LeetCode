# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def findDepth(node):
            if node is None:
                return 0
            left = findDepth(node.left)
            right = findDepth(node.right)
            if left == 0 or right == 0:
                return left + right + 1
            else:
                return min(left, right) + 1
        
        return findDepth(root)