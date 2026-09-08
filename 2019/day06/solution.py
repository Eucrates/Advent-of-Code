# adventofcode.com 2019 day 6
# used gemeni to help implement the tree and path finding between nodes

import sys

if len(sys.argv) != 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

        
    def print_tree(self, depth=0):
        indent = "  " * depth
        prefix = indent + "|__ " if depth > 0 else ""
        print(f"{prefix}{self.data}")
        for child in self.children:
            child.print_tree(depth + 1)

def find_and_add_child_dfs(current_node, target_value, new_child_value):
    if not current_node: return False

    if current_node.data == target_value:
        current_node.add_child(TreeNode(new_child_value))
        return True

    for child in current_node.children:
        if find_and_add_child_dfs(child, target_value, new_child_value):
            return True
    return False

def find_path_from_root(root, target, current_path):
    if root is None:
        return False

    current_path.append(root)

    if root == target:
        return True

    for child in root.children:
        if find_path_from_root(child, target, current_path):
            return True

    current_path.pop()
    return False

def find_path(root, node_a, node_b):
    path_a = []
    path_b = []

    if not find_path_from_root(root, node_a, path_a) or not find_path_from_root(root, node_b, path_b):
        return None

    lca = 0
    while lca < len(path_a) and lca < len(path_b):
        if path_a[lca] == path_b[lca]:
            lca += 1
        else:
            break

    up_path = path_a[lca-1:][::-1]
    down_path = path_b[lca:]

    full_path = up_path + down_path

    return [node.data for node in full_path]

def find_and_return_node_dfs(current_node,target_value):

    if current_node is None: return None

    if current_node.data == target_value:
        return current_node

    for child in current_node.children:
        found_node = find_and_return_node_dfs(child, target_value)
        if found_node:
            return found_node
    return None

def count_nodes(node):
    if not node:
        return 0
    total = 1
    for child in node.children:
        total += cound_total_nodes(child)

    return total

def steps_to_nodes(node, current_steps=0,step_map=None):
    if step_map is None:
        step_map = {}
    if not node:
        return step_map

    step_map[node.data] = current_steps

    for child in node.children:
        steps_to_nodes(child, current_steps + 1, step_map)

    return step_map


root = TreeNode("COM")

planets = []
for line in lines:
    line = line.strip("\n")
    orbitee,orbiter = line.split(")")
    planets.append([orbitee,orbiter])


# Very slow, but wasn't sure how else to sort the planets to add them properly 
i = 0
while i < len(planets):
    orbitee,orbiter = planets[i]
    if find_and_add_child_dfs(root,orbitee,orbiter):
        planets.remove([orbitee,orbiter])
        i = 0
        continue
    i += 1


#root.print_tree()
steps_required = steps_to_nodes(root)
tot_orbits = 0
for node,steps in steps_required.items():
    tot_orbits += steps

print(f"Part 1: {tot_orbits}")
you = find_and_return_node_dfs(root,"YOU")
san = find_and_return_node_dfs(root,"SAN")
lca = find_path(root, you, san)
print(f"Part 2: {len(lca)-3}")
