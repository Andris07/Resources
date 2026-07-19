from collections import deque
from CodeExamples.adjacency_matrix import Graph
from CodeExamples.node import Node

# Algorithm
def breadth_first_search(graph, start):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    print()

    while queue:
        current = queue.popleft()

        print(current)

        for neighbor in graph.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def main():
    graph = Graph(5)

    graph.add_node(Node("A"))
    graph.add_node(Node("B"))
    graph.add_node(Node("C"))
    graph.add_node(Node("D"))
    graph.add_node(Node("E"))

    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    breadth_first_search(graph, graph.nodes[0])

if __name__ == "__main__":
    main()