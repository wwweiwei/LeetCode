# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import numpy as np

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def getList(cur, node):
            val_list = []
            while True:
                val_list.append(cur.val)
                if cur.val < node.val:
                    cur = cur.right
                elif cur.val > node.val:
                    cur = cur.left
                else:
                    return val_list
                
        list_p = getList(root, p)
        list_q = getList(root, q)

        list_p = list_p.reverse()
        list_q = list_q.reverse()
        
        i = 0
        while True:
            if list_p[i] == list_q[i]:
                return list_p[i]
            i += 1      