# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(root):
            if root:
                if root.left is not None or root.right is not None:
                    tmp = root.left
                    root.left = root.right
                    root.right = tmp
                if root.right is not None:
                    invert(root.right)
                if root.left is not None:
                    invert(root.left)
                    
        invert(root)
        
        return root
    