# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None and n == 1:
            return head.next

        cur = head
        len = 0
        while cur:
            len += 1
            cur = cur.next
        
        removal_index = len - n
        if removal_index == 0:
            return head.next
            
        cur = head
        for i in range(removal_index):
            prev = cur
            cur = cur.next
        prev.next = cur.next

        return head



