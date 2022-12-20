"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root == None:
            return None
        preorder_traversal_nodes = []
        preorder_traversal_nodes.append(root.val)
        for each in root.children:
            preorder_traversal_nodes += self.preorder(each)
        return preorder_traversal_nodes
