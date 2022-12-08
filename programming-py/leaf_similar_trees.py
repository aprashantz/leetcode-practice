# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        self.root1_leaves, self.root2_leaves = [], []

        def collect_leaves(root, leaves):
            if root:
                if not root.left and not root.right:
                    leaves.append(root.val)
                else:
                    collect_leaves(root.left, leaves)
                    collect_leaves(root.right, leaves)
        collect_leaves(root1, self.root1_leaves)
        collect_leaves(root2, self.root2_leaves)
        return self.root1_leaves == self.root2_leaves
