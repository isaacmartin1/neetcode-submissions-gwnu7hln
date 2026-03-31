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
            
            left = dfs(node.left) # [20, 100]
            
            right = dfs(node.right) # [0, 0]
            # 3, 20, 100

            left_one_behind = left[0]
            left_two_behind = left[1]
            right_one_behind = right[0]
            right_two_behind = right[1]

            withNode = node.val + left_two_behind + right_two_behind # 3 + 100 + 0

            withoutNode = max(left_one_behind, left_two_behind) + max(right_one_behind, right_two_behind) # 100 + 0

            return [withNode, withoutNode] # [103, 100]


        return max(dfs(root))





