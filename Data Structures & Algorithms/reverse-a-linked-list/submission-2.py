# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_saved = curr.next
            curr.next = prev
            prev = curr
            curr = next_saved
        # return prev bc curr is none in order to exit and prev has the references to go all the way back
        return prev
