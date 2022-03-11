# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        id(): memory addr
        '''
        existed = {}
        while head:
            if id(head) not in existed:
                existed[id(head)] = True
            else:
                return True
            head = head.next
        return False