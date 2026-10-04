#         A
#       /   \
#      B     C
#     / \     \
#    D   E     F
# BFS visits nodes in this order:
# A, B, C, D, E, F
# Start: [A]

# Process A
# Add B, C
# Queue: [B, C]

# Process B
# Add D, E
# Queue: [C, D, E]

# Process C
# Add F
# Queue: [D, E, F]
# graph = {
#     "A": ["B", "C"],
#     "B": ["D", "E"],
#     "C": ["F"],
#     "D": [],
#     "E": [],
#     "F": []
# }
# Suppose we have this relationship map, Your job: start from "A" and return nodes in BFS order: ["A", "B", "C", "D", "E", "F"]
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = {start}
    result = []
    
    while queue:
        # add current parent node to the result
        node = queue.popleft()
        result.append(node)
        # add neighbor nodes to queue if
        for neighbor in graph[node]:
          # if we already not visited them >>> cycle in graphs
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result
# print(bfs(graph=graph, start="A"))
# ------------------------------------
# Find the minimum number of edges needed to get from: start to target
    #   A
    #  / \
    # B   C
    # |   |
    # D   E
    #  \ /
    #   F
# A to F? 3
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": ["F"],
    "E": ["F"],
    "F": []
}

def shortest_distance(graph, start, target):
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        # remove node and its current distance
        node, path = queue.popleft()
        # if node is target:
        #     return distance
        if node == target:
          return path

        # examine neighbors
        # for every unvisited neighbor:
        #     mark visited
        #     add (neighbor, distance + 1) to queue
        for neighbor in graph[node]:
          if neighbor not in visited:
            visited.add(neighbor)
            queue.append([neighbor, path + [neighbor]])

    return []
print(shortest_distance(graph=graph, start='A', target='F'))