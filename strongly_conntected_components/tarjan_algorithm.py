from __future__ import annotations
from typing import TypeVar


T = TypeVar("T")


class Vertex:
    def __init__(self, data: T):
        self.data = data
        self.neighbors: list[T] = []
        self.is_visited = False
        self.in_stack = False
        self.index = 0
        self.low_link = 0
        self.vertex_id = 0

    def add_neighbor(self, vertex: Vertex) -> None:
        self.neighbors.append(vertex)

    def __str__(self) -> None:
        return f"Vertex: {self.data} - Group: {self.vertex_id}"


class Tarjan:
    def __init__(self, graph: list[Vertex]) -> None:
        self.graph = graph
        self.stack = []
        self.index = 0
        self.scc_counter = 0

    def find_components(self) -> None:
        for vertex in self.graph:
            if not vertex.is_visited:
                self.dfs(vertex)

    def show_components(self) -> None:
        for vertex in self.graph:
            print(vertex)

    def dfs(self, vertex: Vertex) -> None:
        self.stack.append(vertex)

        vertex.index = self.index
        vertex.low_link = self.index
        vertex.is_visited = True
        vertex.in_stack = True

        self.index += 1

        for neighbor in vertex.neighbors:
            if not neighbor.is_visited:
                self.dfs(neighbor)
                vertex.low_link = min(vertex.low_link, neighbor.low_link)

            elif vertex.in_stack:
                vertex.low_link = min(vertex.low_link, neighbor.index)

        if vertex.index == vertex.low_link:
            while True:
                w = self.stack.pop()
                w.on_stack = False
                w.vertex_id = self.scc_counter

                if w == vertex:
                    break

            self.scc_counter += 1


if __name__ == "__main__":
    v1 = Vertex('1')
    v2 = Vertex('2')
    v3 = Vertex('3')
    v4 = Vertex('4')
    v5 = Vertex('5')
    v6 = Vertex('6')
    v7 = Vertex('7')
    v8 = Vertex('8')

    v1.add_neighbor(v2)
    v2.add_neighbor(v3)
    v2.add_neighbor(v5)
    v2.add_neighbor(v6)
    v3.add_neighbor(v4)
    v3.add_neighbor(v7)
    v4.add_neighbor(v3)
    v4.add_neighbor(v8)
    v5.add_neighbor(v1)
    v5.add_neighbor(v6)
    v6.add_neighbor(v7)
    v7.add_neighbor(v6)
    v8.add_neighbor(v4)
    v8.add_neighbor(v7)

    graph = [v1, v2, v3, v4, v5, v6, v7, v8]

    algorithm = Tarjan(graph)
    algorithm.find_components()
    algorithm.show_components()
