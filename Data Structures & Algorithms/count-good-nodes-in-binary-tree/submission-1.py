# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        if not root:
            return self.res
        
        stack = [[root, root.val]]

        while stack:
            curr, route_max = stack.pop()

            if curr.val >= route_max:
                self.res += 1

            route_max = max(route_max, curr.val)

            if curr.left:
                stack.append([curr.left, route_max])
            if curr.right:
                stack.append([curr.right, route_max])

        return self.res


