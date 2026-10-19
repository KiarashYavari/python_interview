# Topic: Directed Graphs and Topological Sorting
# important difference between directed and undirected graphs!
# In an undirected graph: A ─── B
# You can travel both ways.

# In a directed graph:A ───> B
# You can only travel from A to B.

# Consider: 
# A ───> B ───> C
#         ↑     |
#         |_____|
# This graph contains a directed cycle:

# B → C → B

# However, detecting cycles in directed graphs requires a slightly different technique.

# We cannot simply use the parent-checking approach from undirected graphs.

# Instead, we typically track two sets:
# - visited: Nodes that have already been fully explored.
# - path: Nodes currently in the active DFS recursion path.

# Exercise: Understanding directed cycles
# Consider: 
# graph = {
#     "A": ["B", "C"],
#     "B": ["D"],
#     "C": ["D"],
#     "D": []
# }

#    A
#   / \
#  v   v
#  B   C
#   \ /
#    v
#    D

# Suppose we start DFS at A and explore B before C.

# The traversal follows:
# A → B → D


# Directed Cycle Detection
# Consider our graph:
    #    A
    #   / \
    #  v   v
    #  B   C
    #   \ /
    #    v
    #    D
    
# When we perform DFS, we maintain two sets:
# - visited: Nodes that have been completely explored.
# - path: Nodes currently in the active recursion path.

# Here's what happens:
# Step	Action	            visited	        path
# 1	    Enter A	            {}	            {A}
# 2	    Enter B	            {}	            {A, B}
# 3	    Enter D	            {}	            {A, B, D}
# 4	    Finish D	        {D}	            {A, B}
# 5	    Finish B	        {D, B}	        {A}
# 6	    Enter C	            {D, B}	        {A, C}
# 7	    Encounter D again	{D, B}	        {A, C}
# 8	    Finish C	        {D, B, C}	    {A}
# 9	    Finish A	        {A, B, C, D}	{}

# When we encounter D through C: 
# "D" in visited  # True
# "D" in path     # False
# Since D is not in the current recursion path, there is no cycle.

# Now imagine adding this edge:
# graph["D"] = ["A"]
# The graph would contain: A → B → D → A
# When DFS encounters A again: "A" in path  # True
# That indicates a directed cycle.
# The important rule: A directed cycle exists when DFS encounters a node already in its current recursion path.

# Interview Exercise: Detect Cycle in a Directed Graph
# Difficulty: Medium
# Pattern: DFS + Recursion Path Tracking
# Problem Statement
# Given a directed graph represented as an adjacency list, implement a function that returns True if the graph contains a directed cycle and False otherwise.
# Example 1: No cycle
graph1 = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}
# Expected output: False

# Example 2: Contains a cycle
graph2 = {
    "A": ["B"],
    "B": ["C"],
    "C": ["D"],
    "D": ["B"]
}
# Expected output: True

def has_directed_cycle(graph):
    visited = set()
    path = set()

    def dfs(node):
        # Your implementation
        if node in path:
            return True
        
        if node in visited:
            return False
        
        path.add(node)
        
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
            
        path.remove(node)
        visited.add(node)
        
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True

    return False

# print(has_directed_cycle(graph1))

# Always check path before visited.
# This distinguishes an active node (which indicates a cycle when encountered again) from a fully explored node.

# We also moved:
# visited.add(node)

# to the end of DFS.
# This makes visited represent nodes that have been completely explored, consistent with our previous explanation.

# Complexity Analysis

# Complexity	Value	    Explanation
# Time	        O(V + E)	Every vertex and edge is explored at most once
# Space	        O(V)	    Visited set, path set, and recursion stack

#************************************************************
#************************************************************


