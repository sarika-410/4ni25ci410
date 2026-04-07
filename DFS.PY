def dfs(tree, node, visited_order):
    visited_order.append(node)

    for child in tree[node]:
        dfs(tree, child, visited_order)


# Tree representation (adjacency list)
tree = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

# Run DFS
result = []
dfs(tree, 1, result)

# Print output
print("For DFS:", *result)