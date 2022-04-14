# Construct tree from preorder and inorder traversal
# Inorder sequence: D B E A F C
# Preorder sequence: A B D E C F

from __future__ import annotations
from typing import List


class Node:
    def __init__(self, val: int, left: Node = None, right: Node = None):
        self.val: int = val
        self.left: Node = left
        self.right: Node = right


class Tree:

    def build_tree_in_pre(self, preorder: List[int], inorder: List[int]) -> Node:
        if not inorder or not preorder:
            return None

        root: Node = Node(preorder[0])
        mid: int = inorder.index(root.val)
        root.left: Node = self.build_tree_in_pre(preorder[1:mid + 1], inorder[:mid])
        root.right: Node = self.build_tree_in_pre(preorder[mid + 1:], inorder[mid + 1:])

        return root

    def build_tree_in_level(self, levelorder: List[int], inorder: List[int]) -> Node:
        if not inorder or not levelorder:
            return None

        root: Node = Node(levelorder[0])

        mid = inorder.index(root.val)

        iols: List[int] = inorder[:mid + 1]
        iors: List[int] = inorder[mid + 1:]

        lols, lors = [], []

        for element in levelorder[1:]:
            elements = lols if element in iols else lors
            elements.append(element)

        root.left: Node = self.build_tree_in_level(lols, iols)
        root.right: Node = self.build_tree_in_level(lors, iors)
        return root


if __name__ == '__main__':
    print("Build tree from in-order and pre-order")
    tree = Tree()
    root = tree.build_tree_in_pre([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7])
    print(root.val)
    print(root.left.val)
    print(root.right.val)
    print(root.left.left.val)
    print(root.left.right.val)
    print(root.right.left.val)
    print(root.right.right.val)

    print("Build tree from in-order and level-order")
    tree = Tree()
    root = tree.build_tree_in_level([20, 8, 22, 4, 12, 10, 14], [4, 8, 10, 12, 14, 20, 22])
    print(root.val)
    print(root.left.val)
    print(root.right.val)
    print(root.left.left.val)
    print(root.left.right.val)
    print(root.left.right.left.val)
    print(root.left.right.right.val)
