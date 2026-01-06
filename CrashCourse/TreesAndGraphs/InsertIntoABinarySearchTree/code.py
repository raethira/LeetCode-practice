# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def insert(root, new_node):
            if not root:
                return new_node
            
            if root.val > new_node.val:
                root.left = insert(root.left, new_node)
            else:
                root.right = insert(root.right, new_node)

            return root

        new_node = TreeNode(val)
        return insert(root, new_node)
