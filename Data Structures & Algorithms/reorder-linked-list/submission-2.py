# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half
        prev = None
        curr = slow.next
        slow.next = None # cut off first half

        while curr:
            next_saved = curr.next
            curr.next = prev # make this node look backwards
            prev = curr # move prev forward to new valud node
            curr = next_saved # increment current
        
        second = prev
        first = head

        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next
        

