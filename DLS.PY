# Define the Tree Node class
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

# Depth-Limited Search (DLS)
def DLS(node, limit, depth=0):
    if node is None:
        return
    
    # Visit the node
    print(node.value, end=" ")
    
    # Stop if depth limit is reached
    if depth == limit:
        return
    
    # Recur for children
    for child in node.children:
        DLS(child, limit, depth + 1)

# Iterative Deepening DFS (IDDFS)
def IDDFS(root, max_depth):
    for depth in range(max_depth + 1):
        print(f"\nDepth = {depth}:", end=" ")
        DLS(root, depth)

# -----------------------------
# Build the given tree:
#         1
#        / \
#       2   3
#      /|   |\
#     4 5   6 7
# -----------------------------

# Create nodes
root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

# Connect nodes
root.children = [node2, node3]
node2.children = [node4, node5]
node3.children = [node6, node7]

# -----------------------------
# Run DLS
# -----------------------------
print("DLS Traversal (limit = 2):")
DLS(root, 2)

# -----------------------------
# Run IDDFS
# -----------------------------
print("\n\nIDDFS Traversal:")
IDDFS(root, 2)