# Definition for a binary tree node.
import math
class Node:
    def __init__(self, data = 0, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    ## Insert Node
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

class Solution:
    def isValidBST(self, root: Node) -> bool:
        '''
        Given the root of a binary tree, 
        determine if it is a valid binary search tree (BST).
        '''
        ## Wrong answer
        # if root == None:
        #     return True
        # elif root.left!= None and root.left.data >= root.data:
        #     return False
        # elif root.right!= None and root.right.data <= root.data:
        #     return False
        # return self.isValidBST(root.left) and self.isValidBST(root.right)

        def validate(node, low = -math.inf, high = math.inf):
            # Empty trees are valid BSTs.
            if not node:
                return True
            # The current node's value must be between low and high.
            if node.val <= low or node.val >= high:
                return False

            # The left and right subtree must also be valid.
            return (validate(node.right, node.val, high) and validate(node.left, low, node.val))

        return validate(root)
        
if __name__ == "__main__":
    root = Node(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
    sol = Solution()
    print(sol.isValidBST(root))