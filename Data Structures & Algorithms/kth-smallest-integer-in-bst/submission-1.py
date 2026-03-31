# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = 0

        stack = [root]
        visited = set()
        while stack:
            node = stack[-1]
            if not node:
                continue
            if node in visited:
                stack.pop()
            if node.left:
                stack.append(node.left)
            else:
                node = stack.pop()
                visited.add(node)
                self.counter += 1
                for n in stack:
                    print(n.val)
                if self.counter == k:
                    return node.val
                if node.right:
                    stack.append(node.right)

