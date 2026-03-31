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

            left_one_back, left_two_back = dfs(node.left)
            right_one_back, right_two_back = dfs(node.right)

            including_current_node = node.val + left_two_back + right_two_back
            best_excluding_current_node = max(left_one_back, left_two_back) + max(right_one_back, right_two_back)

            return [including_current_node, best_excluding_current_node]

        return max(dfs(root))