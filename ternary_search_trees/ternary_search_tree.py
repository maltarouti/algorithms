from __future__ import annotations
from typing import TypeVar


T = TypeVar("T")


class Node:
    def __init__(self, character: str) -> None:
        self.character = character
        self.left = None
        self.middle = None
        self.right = None
        self.is_leaf = False
        self.value = None


class TernarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def __insert(self,
                 node: Node,
                 key: str,
                 value: T,
                 index: int = 0) -> None:
        character = key[index]

        if node is None:
            node = Node(character)

        if character < node.character:
            node.left = self.__insert(node.left, key, value, index)

        elif character > node.character:
            node.right = self.__insert(node.right, key, value, index)

        elif index < len(key) - 1:
            node.middle = self.__insert(node.middle, key, value, index+1)

        else:
            node.is_leaf = True
            node.value = value

        return node

    def put(self, key: str, value: T) -> None:
        self.root = self.__insert(self.root, key, value)

    def __retrieve(self,
                   node: Node,
                   key: str,
                   index: int = 0) -> Node:

        if node is None:
            return None

        character = key[index]

        if character < node.character:
            return self.__retrieve(node.left, key, index)
        elif character > node.character:
            return self.__retrieve(node.right, key, index)
        elif index < len(key) - 1:
            return self.__retrieve(node.middle, key, index+1)
        else:
            if node.is_leaf:
                return node

    def get(self, key: str) -> T:
        node = self.__retrieve(self.root, key)
        if node:
            return node.value

    def __traverse_tree(self, node: Node, string: str = "") -> Node:
        if node.value:
            print("key: '{}' Value: '{}'".format(string+node.character,
                                                 node.value))

        if node.left:
            self.__traverse_tree(node.left, string)

        if node.middle:
            self.__traverse_tree(node.middle, string+node.character)

        if node.right:
            self.__traverse_tree(node.right, string)

    def traverse(self) -> None:
        if self.root:
            self.__traverse_tree(self.root)


if __name__ == "__main__":
    tree = TernarySearchTree()

    tree.put('cat', 10)
    tree.put('bird', 55)
    tree.put('bee', 20)
    tree.put('cow', 13)

    tree.traverse()
