from collections import deque

def bfs(tree, root):
    visited_order = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        visited_order.append(node)

        # Add children to queue
        for child in tree[node]:
            queue.append(child)

    return visited_order


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

# Run BFS
result = bfs(tree, 1)

# Print output
print("For BFS:", *result)