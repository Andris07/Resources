from node import Node

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    # Add a new vertex
    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    # Add an edge
    def add_edge(self, src, dst):
        if src not in self.adjacency_list or dst not in self.adjacency_list:
            return

        self.adjacency_list[src].append(dst)
        self.adjacency_list[dst].append(src)      # Remove this line for directed graphs

    # Check if an edge exists
    def check_edge(self, src, dst):
        if src not in self.adjacency_list:
            return False

        return dst in self.adjacency_list[src]

    # Print adjacency list
    def print(self):
        for node in self.adjacency_list:
            print(f"{node} -> ", end="")

            for neighbor in self.adjacency_list[node]:
                print(neighbor, end=" -> ")

            print()

graph = Graph()

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")

graph.add_node(A)
graph.add_node(B)
graph.add_node(C)
graph.add_node(D)
graph.add_node(E)

graph.add_edge(A, B)
graph.add_edge(A, C)
graph.add_edge(B, E)
graph.add_edge(C, D)
graph.add_edge(D, E)

graph.print()

print()
print(graph.check_edge(A, C))
print(graph.check_edge(A, E))