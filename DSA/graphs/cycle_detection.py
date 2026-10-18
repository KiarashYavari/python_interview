# Cycle Detection in Graphs
# What is a cycle?
# A cycle exists when we can start at a vertex, follow edges, and return to the same vertex without reusing edges.
# A ----- B
#  \     /
#   \   /
#     C
# This graph contains a cycle:
# A → B → C → A

# But consider:
# A ----- B ----- C
# This graph has no cycle.


# Important: Undirected vs. Directed Graphs
# In an undirected graph, edges work both ways.
graph = {
    "A": ["B"],
    "B": ["A"]
}
# This does not contain a cycle. Going from A to B and immediately back to A simply retraces the same edge.
# That's why cycle detection in undirected graphs requires tracking each node's parent.

# Exercise: Detect Cycle in an Undirected Graph
# Difficulty: Medium
# Technique: DFS + Visited Set + Parent Tracking
# Problem Statement
# Given an undirected graph represented as an adjacency list, determine whether it contains a cycle.
# Return True if a cycle exists; otherwise return False.
# Example 1:
graph = {
    "A": ["B", "C"],
    "B": ["A", "C"],
    "C": ["A", "B"]
}
# Expected output: True

# Example 2:
graph = {
    "A": ["B"],
    "B": ["A", "C"],
    "C": ["B"]
}
# Expected output: False

def has_cycle(graph):
    visited = set()

    def dfs(node, parent):
        # Your implementation
        pass

    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True

    return False