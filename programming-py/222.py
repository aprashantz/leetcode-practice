def count_complete_tree_nodes(root):
    node_count = 0

    def dfs(node):
        if node:
            node_count += 1
            dfs(node.left)
            dfs(node.right)
    dfs(root)
    return node_count


# test below
print(count_complete_tree_nodes([1, 2, 3, 4, 5, 6]))
