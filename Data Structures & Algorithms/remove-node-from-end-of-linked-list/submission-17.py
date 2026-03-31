# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        slow = dummy
        slow.next = head

        fast = head
        # bump fast up a number of nodes such that when it ends the node we want to use to skip is good to go
        while n > 0:
            fast = fast.next
            n -= 1
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        # from one behind the one to skip, skip it
        slow.next = slow.next.next

        return dummy.next