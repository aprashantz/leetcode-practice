# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def sum_left_leaves(root, is_left):
            if not root:
                return 0
            if root.left or root.right:
                return sum_left_leaves(root.left, True) + sum_left_leaves(root.right, False)
            elif is_left:
                return root.val
            else:
                return 0
        return sum_left_leaves(root, False)
