# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def check(root):
            if not root:
                return None
            if root.val > high:
                root = root.left
                return check(root)
            elif root.val < low:
                root = root.right
                return check(root)
            else:
                root.left = check(root.left)
                root.right = check(root.right)
                return root
                
        return check(root)  
        
        # if not root:
        #     return None
        # if root.val > high:
        #     return self.trimBST(root.left, low, high)
        # elif root.val < low:
        #     return self.trimBST(root.right, low, high)
        # else:
        #     root.left = self.trimBST(root.left, low, high)
        #     root.right = self.trimBST(root.right, low, high)
        #     return root
        