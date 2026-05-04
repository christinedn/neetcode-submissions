# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        carry = 0
        cur1, cur2 = l1, l2
        while cur1 or cur2 or carry:
            x = cur1.val if cur1 else 0
            y = cur2.val if cur2 else 0

            total = x + y + carry
            carry = total // 10
            digit = total % 10

            tail.next = ListNode(digit)
            tail = tail.next

            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
        return dummy.next