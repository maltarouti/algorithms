from __future__ import annotations
from typing import TypeVar

T = TypeVar("T")


class Node:
    def __init__(self, node_id: int, data: T) -> None:
        self.node_id: int = node_id
        self.data: T = data
        self.previous_node: Node = None
        self.next_node: Node = None


class DoubleLinkedList:
    def __init__(self) -> None:
        self.head: None = None
        self.tail: None = None


class LRUCache:
    def __init__(self) -> None:
        self.size: int = 0
        self.CAPACITY = 4
        self.cache: dict = {}
        self.linkedlist: DoubleLinkedList = DoubleLinkedList()

    def __str__(self) -> str:
        current_node: Node = self.linkedlist.head
        string: string = ""

        while current_node:
            string += f"{current_node.data}\n"
            current_node = current_node.next_node

        return string

    def __add(self, node: Node) -> None:
        node.next_node = self.linkedlist.head
        node.previous_node = None

        if self.linkedlist.head:
            self.linkedlist.head.previous_node = node

        self.linkedlist.head = node

        if self.linkedlist.tail is None:
            self.linkedlist.tail = node

        self.cache[node.node_id] = node

    def __pop(self) -> None:
        self.linkedlist.tail = self.linkedlist.tail.previous_node
        self.linkedlist.tail.next_node = None

    def __update(self, node: Node) -> None:
        previous_node = node.previous_node
        next_node = node.next_node

        if previous_node:
            previous_node.next_node = next_node
        else:
            self.linkedlist.head = next_node

        if next_node:
            next_node.previous_node = previous_node
        else:
            self.linkedlist.tail = previous_node
        self.__add(node)

    def get(self, node_id: int) -> Node | None:
        if node_id in self.cache:
            node = self.cache.get(node_id)
            self.__update(node)
            return node
        return None

    def put(self, node_id: int, data: T) -> None:
        if node_id in self.cache:
            node = self.cache[node_id]
            node.data = data
            self.__update(node)
        else:
            node = Node(node_id, data)
            if self.size < self.CAPACITY:
                self.size += 1
            else:
                self.__pop()
            self.__add(node)


if __name__ == "__main__":
    cache = LRUCache()

    cache.put(0, 'www.google.com')
    cache.put(1, 'www.facebook.com')
    cache.put(2, 'www.botcords.com')
    cache.put(3, 'www.twitter.com')
    cache.put(4, 'www.instagram.com')
    print(cache)

    cache.get(2)
    print(cache)
