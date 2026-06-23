# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)

        elif root.val == key:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            

            leftmost = root.right
            while leftmost.left is not None:
                leftmost = leftmost.left
            
            root.val = leftmost.val
            root.right = self.deleteNode(root.right, root.val)

        return root

