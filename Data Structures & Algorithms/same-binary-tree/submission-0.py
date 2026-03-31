# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_stack = [p]
        q_stack = [q]

        while q_stack or p_stack:
            q_node = q_stack.pop()
            p_node = p_stack.pop()
        
            if not q_node and not p_node:
                continue
            elif q_node and not p_node:
                return False
            elif p_node and not q_node:
                return False

            if q_node.val != p_node.val:
                return False
            
            q_stack.append(q_node.right)
            p_stack.append(p_node.right)
            q_stack.append(q_node.left)
            p_stack.append(p_node.left)
        
        return True


