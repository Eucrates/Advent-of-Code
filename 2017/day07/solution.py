# Claude AI helped me implement a Multi-way Tree and with most of part 2
import sys

if len(sys.argv) < 2:
    print("Usage: solution.py <filename>")
    sys.exit(1)

file = sys.argv[1]

with open (file) as f:
    lines = f.readlines()[:-1] # assumes input ends in newline


class Node:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.children = []

    def total_weight(self):
        return self.weight + sum(c.total_weight() for c in self.children)

def total_weight(node):
    return node.weight + sum (total_weight(c) for c in node.children)

def balance_node(node):
    child_weights = [total_weight(c) for c in node.children]

    if len(set(child_weights)) > 1:
        for i, child in enumerate(node.children):
            if child_weights.count(child_weights[i]) == 1:
                result = balance_node(child)
                if result:
                    return result

                target = next(w for w in child_weights if child_weights.count(w) > 1)
                return child.name, child.weight + (target - child_weights[i])
    return None


stack = {}
all_discs = set()

for line in lines:
    line = line.strip("\n")
    
    parts = line.split(" (")
    name = parts[0].strip()
    weight = int(parts[1].split(")")[0])
    stack[name] = Node(name, weight)

    if "->" in line: 
        children = [c.strip() for c in line.split(" -> ")[1].split(",")]
        stack[name].temp_children = children
        all_discs.update(children)

for name, node in stack.items():
    if hasattr(node, 'temp_children'):
        node.children = [stack[c] for c in node.temp_children]

root_name = (set(stack.keys()) - all_discs).pop()
root = stack[root_name]


print(f"Part 1: {root.name}")
print(f"Part 2: {balance_node(root)[1]}")
