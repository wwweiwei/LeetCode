# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
##        error!!
#         head = l1
#         tmp = 0
#         last_l1 = l1

#         while True:
#             if l1 is not None and l2 is not None:
#                 cur_sum = int(l1.val+l2.val+tmp)
#                 if cur_sum < 10:
#                     l1.val = cur_sum
#                     tmp = 0
#                 else:
#                     tmp = cur_sum / 10
#                     l1.val = cur_sum % 10
#                 last_l1 = l1
#                 l1 = l1.next
#                 l2 = l2.next
#             elif l1 is not None:
#                 cur_sum = int(l1.val+tmp)
#                 if cur_sum < 10:
#                     l1.val = cur_sum
#                     tmp = 0
#                 else:
#                     tmp = cur_sum / 10
#                     l1.val = cur_sum % 10
#                 last_l1 = l1
#                 l1 = l1.next
#             elif l2 is not None:
#                 l1 = l2
#                 cur_sum = int(l2.val+tmp)
#                 if cur_sum < 10:
#                     l1.val = cur_sum
#                     tmp = 0
#                 else:
#                     tmp = cur_sum / 10
#                     l1.val = cur_sum % 10
#                 l2 = l2.next
#             else:
#                 if tmp != 0:
#                     last_l1.next = ListNode(val=int(tmp))
#                 return head

            result = ListNode(0)
            node = result
            temp = 0
            
            while l1 is not None or l2 is not None or temp>0:
                if l1 is not None:
                    temp += l1.val
                    l1 = l1.next
                if l2 is not None:
                    temp += l2.val
                    l2 = l2.next
                node.next = ListNode(temp%10)
                node = node.next
                temp = temp // 10
            return result.next
                  