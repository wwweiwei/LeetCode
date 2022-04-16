# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.sum_ = 0
        '''
        traverse from biggest to smallest
        add the value in order to sum_
        and update the value in order by sum_
        '''
        def bigtosmall(cur):
            if cur is None:
                return
            bigtosmall(cur.right)
            self.sum_ += cur.val
            cur.val = self.sum_
            bigtosmall(cur.left)
        
        bigtosmall(root)
        
        return root
