# Weighted Graphs
# Unlike our previous graphs, where every edge had the same cost, weighted graphs assign a numerical cost to each edge.

# An undirected weighted graph. Numbers represent edge costs.

# Suppose we want to find the shortest path from A to D.

# There are three possible paths:
# Path	    Total cost
# A → D	        10
# A → B → D	    2 + 4 = 6
# A → C → D	    5 + 1 = 6

# Dijkstra's Algorithm
# Before we implement Dijkstra's algorithm, here's a quick conceptual question.

# Question: Why is BFS insufficient for finding the minimum-cost path in a weighted graph?

# Answer: Because BFS minimizes the number of edges, not the sum of edge weights.

# Dijkstra's algorithm finds the minimum-cost paths from a starting node to every other reachable node in a weighted graph.

# Important: Standard Dijkstra's algorithm requires non-negative edge weights.

# Consider this graph:
#        2          4
#   A -------- B -------- D
#   |          |          |
#   | 5        | 1        | 2
#   |          |          |
#   C -------- E -------- F
#        3          1

# We'll represent it using a weighted adjacency list:

# graph = {
#     "A": [("B", 2), ("C", 5)],
#     "B": [("D", 4), ("E", 1)],
#     "C": [("E", 3)],
#     "D": [("F", 2)],
#     "E": [("F", 1)],
#     "F": []
# }

# For this exercise, we'll treat the graph as directed, following the adjacency list.
