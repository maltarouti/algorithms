from __future__ import annotations
from typing import TypeVar


T = TypeVar("T")


class Node:
    def __init__(self, data: T, parent: Node = None) -> None:
        self.data: T = data
        self.parent: Node = parent
        self.right: Node = None
        self.left: Node = None


class SplayTree:
    def __init__(self):
        self.root: Node = None

    def find(self, data: T) -> Node:
        node = self.root

        while node is not None:
            if data < node.data:
                node = node.left
            elif data > node.data:
                node = node.right
            else:
                self.__splay(node)
                return node.data

    def insert(self, data: T):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.__insert(data, self.root)

    def __insert(self, data: T, node: Node) -> Node:
        if data < node.data:
            if node.left:
                self.__insert(data, node.left)
            else:
                node.left = Node(data, node)
        else:
            if node.right:
                self.__insert(data, node.right)
            else:
                node.right = Node(data, node)

    def __splay(self, node):
        while node.parent is not None:
            # Zig: The node is left or right child of root node
            if node.parent.parent is None:
                if node == node.parent.left:
                    self.__rotate_right(node.parent)
                else:
                    self.__rotate_left(node.parent)

            # Zig Zig: The node is the left child of parent and the parent is
            # left of grand parent
            elif (node == node.parent.left
                  and node.parent == node.parent.parent.left):
                self.__rotate_right(node.parent.parent)
                self.__rotate_right(node.parent)

            elif (node == node.parent.right
                  and node.parent == node.parent.parent.right):
                self.__rotate_left(node.parent.parent)
                self.__rotate_left(node.parent)

            # Zig Zag: The node is the right child of parent and the parent
            # is the left
            elif (node == node.parent.left
                  and node.parent == node.parent.parent.right):
                self.__rotate_right(node.parent)
                self.__rotate_left(node.parent)
            else:
                self.__rotate_left(node.parent)
                self.__rotate_right(node.parent)

    def __rotate_right(self, node: Node) -> None:
        temp_left_node = node.left
        temp_right_side = temp_left_node.right

        temp_left_node.right = node
        node.left = temp_right_side

        if temp_right_side is not None:
            temp_right_side.parent = node

        temp_parent = node.parent
        node.parent = temp_left_node
        temp_left_node.parent = temp_parent

        if temp_left_node.parent and temp_left_node.parent.left == node:
            temp_left_node.parent.left = temp_left_node

        if temp_left_node.parent and temp_left_node.parent.right == node:
            temp_left_node.parent.right = temp_left_node

        if node == self.root:
            self.root = temp_left_node

    def __rotate_left(self, node: Node) -> None:
        temp_right_node = node.right
        temp_left_side = temp_right_node.left

        temp_right_node.left = node
        node.right = temp_left_side

        if temp_left_side:
            temp_left_side.parent = node

        temp_parent = node.parent
        node.parent = temp_right_node
        temp_right_node.parent = temp_parent

        if temp_right_node.parent and temp_right_node.parent.left == node:
            temp_right_node.parent.left = temp_right_node

        if temp_right_node.parent and temp_right_node.parent.right == node:
            temp_right_node.parent.right = temp_right_node

        if node == self.root:
            self.root = temp_right_node


if __name__ == "__main__":
    splay_tree = SplayTree()
    splay_tree.insert(10)
    splay_tree.insert(8)
    splay_tree.insert(3)
    splay_tree.insert(7)
    splay_tree.insert(1)

    splay_tree.find(1)
    print(splay_tree.root.data)
