from __future__ import annotations
from typing import TypeVar

T = TypeVar("T")


class Vertex:
    def __init__(self, data: T) -> None:
        self.data = data
        self.is_visited = False
        self.neighbors: list[Vertex] = []

    def add_neighbor(self, vertex: Vertex) -> None:
        self.neighbors.append(vertex)

    def __str__(self) -> str:
        return self.data


class TopologicalOrdering:
    def __init__(self) -> None:
        self.stack = []

    def dfs(self, vertex: Vertex):
        vertex.is_visited = True

        for neighbor in vertex.neighbors:
            if not neighbor.is_visited:
                self.dfs(neighbor)

        self.stack.append(vertex)

    def order_vertices(self, graph: list[Vertex]) -> None:
        for vertex in graph:
            if not vertex.is_visited:
                ordering.dfs(vertex)

    def get_ordering(self, reverse=False) -> list[Vertex]:
        if reverse:
            return self.stack[::-1]
        return self.stack


if __name__ == "__main__":
    graph = [
        Vertex('0'),
        Vertex('1'),
        Vertex('2'),
        Vertex('3'),
        Vertex('4'),
        Vertex('5'),
    ]

    graph[2].add_neighbor(graph[3])
    graph[3].add_neighbor(graph[1])
    graph[4].add_neighbor(graph[0])
    graph[4].add_neighbor(graph[1])
    graph[5].add_neighbor(graph[0])
    graph[5].add_neighbor(graph[2])

    ordering = TopologicalOrdering()
    ordering.order_vertices(graph)

    for vertex in ordering.get_ordering(reverse=True):
        print(vertex)
