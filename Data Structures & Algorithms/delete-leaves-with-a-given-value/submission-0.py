# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
DELETE = "delete"
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if root.left:
            left_del = self.removeLeafNodes(root.left, target)
            if left_del == None:
                root.left = None
        
        if root.right:
            right_del = self.removeLeafNodes(root.right, target)
            if right_del == None:
                root.right = None 

        if self.is_leaf(root) and root.val == target:
            return None

        return root
    
    def is_leaf(self, node: TreeNode):
        if node.left is None and node.right is None:
            return True
        return False