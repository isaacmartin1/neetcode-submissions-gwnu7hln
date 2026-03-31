# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = [[0, root]]
        res = [[]]

        while stack:
            depth, node = stack.pop()
            
            if not node:
                continue
            
            if depth > len(res) - 1:
                res.append([])

            res[depth].append(node.val)
            if node.right:
                stack.append([depth+1, node.right])
            if node.left:
                stack.append([depth+1, node.left])
            

        
        print(res)
        return res
