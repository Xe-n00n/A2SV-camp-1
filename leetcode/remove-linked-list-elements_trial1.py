# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prev = dummy
        x = head
        while x:
            if x.val == val:
                prev.next = x.next
            else:
                prev = x
            x = x.next
        
        return dummy.next

        