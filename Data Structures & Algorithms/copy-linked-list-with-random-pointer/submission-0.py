"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copied_list = { None : None}
        
        curr = head
        # copy indexes
        while curr:
            copy = Node(curr.val)
            copied_list[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = copied_list[curr]
            copy.next = copied_list[curr.next]
            copy.random = copied_list[curr.random]
            curr = curr.next
        
        return copied_list[head]

