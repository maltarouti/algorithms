from __future__ import annotations
from typing import TypeVar


T = TypeVar("T")
ALPHABET_SIZE: int = 128


class Node:
    def __init__(self, character: str) -> None:
        self.character = character
        self.children = [None] * ALPHABET_SIZE
        self.is_leaf = False
        self.value: T = None


class Trie:
    def __init__(self) -> None:
        self.root = Node("*")

    def insert(self, key: str, value: T) -> None:
        current = self.root

        for letter in key:
            ascii_index = ord(letter)

            if current.children[ascii_index] is not None:
                current = current.children[ascii_index]

            else:
                node = Node(letter)
                current.children[ascii_index] = node
                current = node

        current.is_leaf = True
        current.value = value

    def get(self, key: str) -> T | None:
        if not self.root.children:
            return False

        current = self.root

        for letter in key:
            ascii_index = ord(letter)

            if current.children[ascii_index]:
                current = current.children[ascii_index]
            else:
                return None

        if current.is_leaf:
            return current.value
        return None

    def sort(self):
        return self.get_words_prefix('')

    def get_words_prefix(self, prefix: str) -> list[str]:
        words = []
        node = self.root

        for letter in prefix:
            ascii_index = ord(letter)

            if node.children[ascii_index] is None:
                return None

            node = node.children[ascii_index]

        self.collect(node, prefix, words)
        return words

    def collect(self, node: Node,
                prefix: str,
                words: list[str]):
        if node is None:
            return

        if node.is_leaf:
            words.append(prefix)

        for child in node.children:
            if not child:
                continue

            child_character = child.character
            self.collect(child, prefix+child_character, words)


if __name__ == "__main__":
    trie = Trie()
    trie.insert("cube", 2)
    trie.insert("stone", 5)
    trie.insert("tree", 12)
    trie.insert("send", 3)

    print("All words in the trie tree are: ", trie.sort())

    word = 'cube'
    print(f"The value word'{word}' is", trie.get(word))

    prefix = "s"
    print(f"The words with {prefix} prefix are: ",
          trie.get_words_prefix(prefix))
