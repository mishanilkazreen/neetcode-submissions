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

        s_head = slow.next
        slow.next = prev = None
        while s_head:
            temp = s_head.next
            s_head.next = prev
            prev = s_head
            s_head = temp

        l, r = head, prev
        while r:
            nextl, nextr = l.next, r.next
            l.next = r
            r.next = nextl
            l = nextl
            r = nextr
        