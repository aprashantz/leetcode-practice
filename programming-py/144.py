# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder_traversal = []
        if not root:
            return preorder_traversal

        def preorder(node):
            if node:
                preorder_traversal.append(node.val)
                preorder(node.left)
                preorder(node.right)

        preorder(root)
        return preorder_traversal

        # return [] if not root else [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
