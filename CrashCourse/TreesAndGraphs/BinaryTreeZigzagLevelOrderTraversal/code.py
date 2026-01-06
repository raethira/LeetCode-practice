# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        queue = deque([root])
        ans = []
        direction = 1

        while queue:
            current_length = len(queue)
            level = []
            
            for _ in range(current_length):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if direction % 2 == 0:
                level = level[::-1]

            ans.append(level)
            direction += 1

        return ans
    
