# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.smallest = float("inf")
        self.smallestKey = 0

        def dfs(node):
            if not node:
                return None
            
            diff = abs(node.val - abs(target))
            if self.smallest > diff:
                self.smallest = diff
                self.smallestKey = node.val
            
            if diff == self.smallest and node.val < self.smallestKey:
                self.smallestKey = node.val

            if target <= node.val:
                dfs(node.left)
            else:    
                dfs(node.right)

            return self.smallestKey

        return dfs(root)
