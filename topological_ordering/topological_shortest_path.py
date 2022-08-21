from __future__ import annotations
from typing import TypeVar

import sys


MAX_VALUE = sys.maxsize
T = TypeVar("T")


class Vertex:
    def __init__(self, data: T) -> None:
        self.data = data
        self.is_visited = False
        self.min_distance = MAX_VALUE
        self.predecessor: Vertex | None = None
        self.neighbors: list[Vertex] = []

    def add_neighbor(self, vertex: Vertex) -> None:
        self.neighbors.append(vertex)

    def __str__(self):
        return f"{self.data} - {self.predecessor}"


class Edge:
    def __init__(self,
                 target: Vertex,
                 weight: int) -> None:
        self.target = target
        self.weight = weight


class TopologicalOrdering:
    def __init__(self, graph: list[Vertex]):
        self.graph = graph
        self.stack = []

    def order_vertices(self) -> None:
        for vertex in self.graph:
            if not vertex.is_visited:
                self.dfs(vertex)

    def dfs(self, vertex: Vertex) -> None:
        vertex.is_visited = True

        for neighbor in vertex.neighbors:
            if not neighbor.target.is_visited:
                self.dfs(neighbor.target)
        self.stack.append(vertex)

    def get_ordering(self, reverse=False) -> list[Vertex]:
        if reverse:
            return self.stack[::-1]
        return self.stack


class ShortestPath:
    def __init__(self, graph: list[Vertex]) -> None:
        self.graph = graph
        self.topological_ordering = TopologicalOrdering(graph)

    def find_shortest_path(self):
        self.topological_ordering.order_vertices()
        stack = self.topological_ordering.get_ordering()

        self.graph[0].min_distance = 0
        while stack:
            u = stack.pop()

            for edge in u.neighbors:
                v = edge.target

                if u.min_distance + edge.weight < v.min_distance:
                    v.min_distance = u.min_distance + edge.weight
                    v.predecessor = u


if __name__ == '__main__':
    v0 = Vertex('S')
    v1 = Vertex('A')
    v2 = Vertex('B')
    v3 = Vertex('C')
    v4 = Vertex('D')
    v5 = Vertex('E')

    v0.neighbors.append(Edge(v1, 1))
    v0.neighbors.append(Edge(v3, 2))

    v1.neighbors.append(Edge(v2, 6))

    v2.neighbors.append(Edge(v4, 1))
    v2.neighbors.append(Edge(v5, 2))

    v3.neighbors.append(Edge(v1, 4))
    v3.neighbors.append(Edge(v4, 3))

    v4.neighbors.append(Edge(v5, 1))

    graph = [v0, v1, v2, v3, v4, v5]

    algorithm = ShortestPath(graph)
    algorithm.find_shortest_path()

    for vertex in graph:
        print(f'Distance from S: {vertex.min_distance} - {vertex}')
