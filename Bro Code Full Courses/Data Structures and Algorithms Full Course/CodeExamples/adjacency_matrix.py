from CodeExamples.node import Node

class Graph:
    def __init__(self, size):
        self.nodes = []
        self.matrix = [[0 for _ in range(size)] for _ in range(size)]

    # Add a new vertex
    def add_node(self, node):
        self.nodes.append(node)

    # Add an edge
    def add_edge(self, src, dst):
        if src >= len(self.nodes) or dst >= len(self.nodes):
            return

        self.matrix[src][dst] = 1
        self.matrix[dst][src] = 1      # Remove this line for directed graphs

    # Check if an edge exists
    def check_edge(self, src, dst):
        if src >= len(self.nodes) or dst >= len(self.nodes):
            return False

        return self.matrix[src][dst] == 1

    # Print adjacency matrix
    def print(self):
        print(" ", end=" ")

        for node in self.nodes:
            print(node, end=" ")

        print()

        for i in range(len(self.nodes)):
            print(self.nodes[i], end=" ")

            for value in self.matrix[i]:
                print(value, end=" ")

            print()

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

graph.print()

print()
print(graph.check_edge(0, 2))
print(graph.check_edge(0, 4))