from CodeExamples.adjacency_list import Graph
from CodeExamples.node import Node

# Algorithm
def depth_first_search(graph, node):
    visited = set()
    print()
    _dfs(graph, node, visited)

def _dfs(graph, node, visited):
    if node in visited:
        return
    
    visited.add(node)

    print(node)

    for neighbor in graph.get_neighbors(node):
        _dfs(graph, neighbor, visited)

graph = Graph()

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")

graph.add_node(A)
graph.add_node(B)
graph.add_node(C)
graph.add_node(D)
graph.add_node(E)
graph.add_node(F)

graph.add_edge(A, B)
graph.add_edge(A, C)
graph.add_edge(B, D)
graph.add_edge(C, E)
graph.add_edge(E, F)

depth_first_search(graph, A)