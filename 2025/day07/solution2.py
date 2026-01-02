class Node:
    """Represents a single node in the binary tree."""
    def __init__(self, path_value):
        self.path_value = path_value
        self.left = None
        self.right = None

class BinaryTreePath:
    """Manages the binary tree structure and provides counting methods."""
    def __init__(self):
        self.root = Node("") # Root node has an empty path

    def _insert_recursive(self, current_node, path_segment):
        """Helper method to insert nodes recursively based on path segments."""
        if path_segment == 'L':
            if current_node.left is None:
                current_node.left = Node(current_node.path_value + 'L')
            else:
                self._insert_recursive(current_node.left, path_segment)
        elif path_segment == 'R':
            if current_node.right is None:
                current_node.right = Node(current_node.path_value + 'R')
            else:
                self._insert_recursive(current_node.right, path_segment)

    def insert(self, full_path):
        """Inserts a new node into the tree by traversing its intended path."""
        if not full_path:
            return # Root already exists

        current = self.root
        for i, segment in enumerate(full_path):
            # If it's the last segment, the node should be inserted as a child
            if i == len(full_path) - 1:
                if segment == 'L':
                    if current.left is None:
                        current.left = Node(full_path)
                    else:
                        # Node at this path already exists
                        pass 
                elif segment == 'R':
                    if current.right is None:
                        current.right = Node(full_path)
                    else:
                        # Node at this path already exists
                        pass
                break
            # Traverse down the tree
            if segment == 'L':
                if current.left is None:
                    # Automatically create intermediate nodes if they don't exist
                    current.left = Node(current.path_value + 'L')
                current = current.left
            elif segment == 'R':
                if current.right is None:
                    # Automatically create intermediate nodes if they don't exist
                    current.right = Node(current.path_value + 'R')
                current = current.right

    def _count_nodes_recursive(self, node):
        """Recursively counts all nodes in the tree."""
        if node is None:
            return 0
        return 1 + self._count_nodes_recursive(node.left) + self._count_nodes_recursive(node.right)

    def count_total_nodes(self):
        """Returns the total number of nodes in the tree."""
        return self._count_nodes_recursive(self.root)

    def count_total_paths(self):
        """Returns the total number of paths from the root to any existing node (same as total nodes)."""
        return self.count_total_nodes()

    def _count_leaf_nodes_recursive(self, node):
        """Recursively counts leaf nodes (bottom nodes)."""
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self._count_leaf_nodes_recursive(node.left) + self._count_leaf_nodes_recursive(node.right)

    def count_bottom_nodes(self):
        """Returns the total number of bottom (leaf) nodes in the tree."""
        # Handle the edge case of an empty tree (only root with no children)
        if self.root is None or (self.root.left is None and self.root.right is None and self.root.path_value == ""):
            return 0
        return self._count_leaf_nodes_recursive(self.root)


# Example Usage: Building a tree
tree = BinaryTreePath()

# Insert paths to simulate a tree up to a certain depth
paths_to_insert = [
    'L', 'R', 
    'LL', 'LR', 'RL', 'RR', 
    'LLL', 'LLR', 'LRL', 'LRR', 'RLL', 'RLR', 'RRL', 'RRR'
]

# This creates a full binary tree of depth 3
for path in paths_to_insert:
    tree.insert(path)

# Add some deeper nodes to show counting on a non-full tree
tree.insert('LLLL')
tree.insert('LLLR')


print(f"Total Nodes: {tree.count_total_nodes()}")
print(f"Total Paths (to existing nodes): {tree.count_total_paths()}")
print(f"Total Bottom (Leaf) Nodes: {tree.count_bottom_nodes()}")


