# Construct tree from preorder and inorder traversal
# Inorder sequence: D B E A F C
# Preorder sequence: A B D E C F

from __future__ import annotations


class Node:
    def __init__(self, val: int, left: Node = None, right: Node = None):
        self.val: int = val
        self.left: Node = left
        self.right: Node = right


class Tree:

    def __init__(self, root):
        self.root = root
        self.curr = None

    def in_order(self, val: str):
        if self.root is None:
            self.curr = Node(val)
        else:

