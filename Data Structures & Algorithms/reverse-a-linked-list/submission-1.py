# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        dummy = None
        first = head
        second = head.next
        while second != None:
            first.next = dummy
            dummy = first
            first = second
            second = second.next
        first.next = dummy
        return first