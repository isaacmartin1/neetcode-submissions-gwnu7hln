# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:        

        def dfs(node):
            if not node:
                return [0, 0]
            
            left = dfs(node.left) # [100, 0]
            
            right = dfs(node.right) # [0, 0]
            # 3, 20, 100

            withNode = node.val + left[1] + right[1] # 20 + 0 + 0
            withoutNode = max(left) + max(right) # 100 + 0

            return [withNode, withoutNode] # [20, 100]


        return max(dfs(root))





