# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        length_counter = head
        while length_counter:
            length += 1
            length_counter = length_counter.next
            
        print('length', length, 'n', n)
        del_n_idx = length - n
        print('del n index', del_n_idx)

        res = ListNode()
        res.next = head
        prev = res

        if not head.next:
            return None
        i = 0
        while head:
            print('lllllllllllllllllllllllllllllll')
            print('prev', prev)
            if prev:
                print(prev.val)
            print('head', head)
            if head:
                print(head.val)
            
            if del_n_idx == i:
                print('delete block is at index', i)
                prev.next = head.next
                if head.next:
                    head = head.next.next
            else:
                print(del_n_idx, i)
                prev = head
                head = head.next
            i += 1
        return res.next
        