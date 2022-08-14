
from platform import node
from typing import List


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root: List[Node]=None) -> None:
        self.root = root

    # def in_order_make_tree(self, nodes: List[Node]) 

    def in_order(self) -> List:
        path = []
        if self.root
        self._in_order_helper(self.root, path)
        return path

    def _in_order_helper(self, node: Node, path: List) -> None:

        if node.left:
            self._in_order_helper(node.left, path)
        path.append(node.val)
        if node.right:
            self._in_order_helper(node.right, path)

f = Node('F')
b = Node('B')
g = Node('G')
f.left = b
f.right = g
a = Node('A')
d = Node('D')
h = Node('H')
b.left = a
b.right = d
g.right = h
c = Node('C')
e = Node('E')
d.left = c
d.right = e

tree = Tree(f)
path = tree.in_order()
print(path)
