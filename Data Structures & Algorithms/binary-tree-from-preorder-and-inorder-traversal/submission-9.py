# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        node = TreeNode(preorder[0])
        split_idx = inorder.index(preorder[0])

        node.left = self.buildTree(preorder[1:split_idx + 1], inorder[:split_idx])
        node.right = self.buildTree(preorder[split_idx + 1:], inorder[split_idx + 1:])


        return node