# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ans = []
        def check(root):
            if root.left:
                # ans.insert(0, root.left.val)
                check(root.left)
            ans.append(root.val)
            if root.right:
                # ans.append(root.right.val)
                check(root.right)
            return
        check(root)
        
        format_ans = []
        while ans:
            format_ans.append(ans.pop(0))
            format_ans.append(None)
            
        return format_ans
        