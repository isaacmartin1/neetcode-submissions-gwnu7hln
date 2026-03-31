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
        copy_hash = {None: None}

        curr = head
        while curr:
            copy = Node(curr.val)
            copy_hash[curr] = copy
            curr = curr.next
        

        curr = head
        while curr:
            copy = copy_hash[curr]
            copy.next = copy_hash[curr.next]
            copy.random = copy_hash[curr.random]
            curr = curr.next
        
        return copy_hash[head]
        

