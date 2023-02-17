# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        all_nodes = []

        def return_by_dfs(root):
            if root:
                all_nodes.append(root.val)
                return_by_dfs(root.left)
                return_by_dfs(root.right)
        return_by_dfs(root)
        all_nodes = sorted(all_nodes)
        min_dis = all_nodes[-1]
        for i in range(len(all_nodes)-1):
            cur_nodes_dis = abs(all_nodes[i] - all_nodes[i+1])
            if cur_nodes_dis < min_dis:
                min_dis = cur_nodes_dis
        return min_dis
