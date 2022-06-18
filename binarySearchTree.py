
from typing import Tuple


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# format : leftnode, root, rightnode
data = ((1,3,None),2,((None,3,4),5,(6,7,8)))

#create binary tree
def generate_tree(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = Node(data[1])
        node.left = generate_tree(data[0])
        node.right = generate_tree(data[2])
    elif data is None:
        node = None
    else:
        node = Node(data)
    return node

output_tree = generate_tree(data)

#convert tree to tuple to check output
def tree_to_tuple(data_input) -> Tuple[int]:
    if isinstance(data_input, Node):
        if data_input.left is None and data_input.right is None:
            return data_input.key
        return (
            tree_to_tuple(data_input.left), 
            data_input.key, 
            tree_to_tuple(data_input.right)
            )

tuple_out = tree_to_tuple(output_tree)
print(tuple_out)