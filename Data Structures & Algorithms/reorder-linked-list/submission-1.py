# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # at this point, slow will be pointing to the middle. fast will be at the end
        # we want to split it at slow.next
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge the two halfs
        first, second = head, prev
        while second: # do while second == null because second is the pointer that is at the end of the list. first will technically never be null?
            tmp1, tmp2 = first.next, second.next 
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2


            
        