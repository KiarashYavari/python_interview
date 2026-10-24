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

# How Dijkstra Works
# Imagine we're starting from node A.

# Initially, we don't know the shortest distances to any other nodes.

# We initialize:

# distances = {
#     "A": 0,
#     "B": float("inf"),
#     "C": float("inf"),
#     "D": float("inf"),
#     "E": float("inf"),
#     "F": float("inf")
# }

# Why?
# - Distance from A to itself is 0.
# - Every other distance is initially unknown, represented by infinity.

# Now comes the important concept.

# At each step, Dijkstra processes the unprocessed node with the smallest currently known distance.
# To efficiently select that node, we use a min-heap (priority queue).

# Python provides this through heapq

import heapq

heap = []

heapq.heappush(heap, (0, "A"))

# The heap stores: (distance, node)
# The smallest distance has the highest priority.

# Step-by-step execution
# Starting from A:
# Step	Node processed	Distance	Updates
# 1	        A	            0	    B = 2, C = 5
# 2	        B	            2	    D = 6, E = 3
# 3	        E	            3	    F = 4
# 4	        F	            4	    None
# 5	        C	            5	    No improvement
# 6	        D	            6	    No improvement

# The shortest path from A to F is: A → B → E → F
# With total cost:
# 2 + 1 + 1 = 4
# Dijkstra finds this because it prioritizes the smallest accumulated cost rather than the fewest edges.

# The Most Important Operation: Relaxation
# In Dijkstra's algorithm, we repeatedly perform an operation called edge relaxation.

# Suppose: 
current_distance = 2
weight = 1

# We calculate:
new_distance = current_distance + weight

# So:
new_distance = 3

# Now we compare it against the previously known distance:
if new_distance < distances[neighbor]:
    distances[neighbor] = new_distance
    
# If we've found a shorter route, we update the distance.
# This is the central operation in Dijkstra's algorithm.