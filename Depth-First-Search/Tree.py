
from platform import node
from typing import List
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root: List[Node]=None) -> None:
        self.root = root

    def pre_order_make_tree(self, nodes: List[Node]):
        node_q = deque(nodes)
        if node_q:
            self.root = self._pre_order_make_tree_helper(node_q)
            
    def _pre_order_make_tree_helper(self, node_q: deque):
        node_val = node_q.popleft()
        if node_val == '':
            return
        node = Node(node_val)
        node.left = self._pre_order_make_tree_helper(node_q)
        node.right = self._pre_order_make_tree_helper(node_q)
        return node
    
    def in_order(self) -> List:
        path = []
        if self.root:
            self._in_order_helper(self.root, path)
        return path

    def _in_order_helper(self, node: Node, path: List) -> None:
        if node.left:
            self._in_order_helper(node.left, path)
        path.append(node.val)
        if node.right:
            self._in_order_helper(node.right, path)

    def pre_order(self) -> List:
        path = []
        if self.root:
            self._pre_order_helper(self.root, path)
        return path

    def _pre_order_helper(self, node: Node, path: List) -> None:
        path.append(node.val)
        if node.left:
            self._pre_order_helper(node.left, path)
        if node.right:
            self._pre_order_helper(node.right, path)

    def post_order(self) -> List:
        path = []
        if self.root:
            self._post_order_helper(self.root, path)
        return path
    
    def _post_order_helper(self, node: Node, path: List) -> None:
        if node.left:
            self._post_order_helper(node.left, path)
        if node.right:
            self._post_order_helper(node.right, path)
        path.append(node.val)

    def dfs(self, root, target):
        if root is None:
            return None
        if root.val == target:
            return root
        left = self.dfs(root.left, target)
        if left:
            return left
        
        return self.dfs(root.right, target)




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
# path = tree.in_order()
# print(path)

tree2 = Tree()
tree2.pre_order_make_tree(['A', 'B', 'C', '', '', 'D', 'E', '', '', 'F', '', '', 'G', '', 'H', '', ''])
# path2 = tree2.pre_order()
# print(path2)

# post_path = tree2.post_order()
# print(post_path)

node = tree2.dfs(tree2.root, 'L')
if node:
    print(node.val)
else:
    print('no node found')
