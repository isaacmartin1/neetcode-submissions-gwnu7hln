# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode()
        dummy.next = head
        # get second half
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the second half
        # slow is now at the halfway point almost
        second = slow.next
        # destroy the connection between first and second half of the original list for now
        slow.next = None
        prev = None
        while second:
            next_second = second.next
            second.next = prev
            prev = second
            second = next_second

        # weave first and second
        first, second = head, prev
        while second:
            next_first = first.next
            next_second = second.next

            first.next = second
            second.next = next_first

            first = next_first
            second = next_second
        