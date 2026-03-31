# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str_1 = ''
        curr_l1 = l1
        while curr_l1:
            str_1 = str(curr_l1.val) + str_1
            curr_l1 = curr_l1.next

        str_2 = ''
        while l2:
            str_2 = str(l2.val) + str_2
            l2 = l2.next
        
        target = str(int(str_1) + int(str_2))
        target_list = []
        for t in target:
            target_list.insert(0, int(t))
    
        dummy = ListNode()
        res = dummy
        
        print(target_list)
        i = 0
        # sacrifice l1
        spare_node = l1
        while i < len(target_list):
            t = target_list[i]
            res.next = ListNode(t)
            res = res.next
            i += 1
        # for t in target_list:
        #     new_node = Node(t)
        #     res.next = new_node
        
        return dummy.next