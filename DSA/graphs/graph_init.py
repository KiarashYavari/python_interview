# A graph consists of:
# - Vertices (nodes): Objects or locations.
# - Edges: Connections between vertices.
# One common way to represent this graph in Python is an adjacency list:
# graph = {
#     "A": ["B", "C"],
#     "B": ["A", "C", "D"],
#     "C": ["A", "B", "D"],
#     "D": ["B", "C"]
# }

# Unlike a tree, a graph can contain cycles, and there doesn't have to be a root node.
# BFS traversal > level by level
# DFS traversal > go deep in one branch then back tracking

# Interview Exercise 1: DFS Graph Traversal
# Difficulty: Easy
# You are given an undirected graph represented as an adjacency list and a starting node.
# Implement a function that performs recursive Depth-First Search (DFS) and returns the nodes in the order they were first visited.
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

start = "A"

def dfs_graph(graph, start):
    visited = set()
    result = []

    def dfs(node):
        if node in visited:
          return 
        if node not in visited:
          visited.add(node)
          result.append(node)
          for neighbor in graph[node]:
            dfs(neighbor)  
            
    dfs(start)
    return result

print(dfs_graph(graph, start))
  
# Complexity	Value	    Reason
# Time	     (O(V+E))	  Each reachable vertex is visited once and its edges are examined
# Space	      (O(V))	  Visited set, result list, and recursion stack
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
# Count Connected Components
# (LeetCode 323 — Medium)
# This problem introduces an important graph concept: connected components.
# A connected component is a group of vertices where every vertex can reach every other vertex in that group.
# Problem statement
# Given an undirected graph represented as an adjacency list, return the number of connected components.
def count_components(graph):
    visited = set()
    count = 0

    # Your implementation

    return count