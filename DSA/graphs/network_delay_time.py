# Problem Statement
# You are given a directed, weighted network of n nodes labeled from 1 to n.

# You also receive:
# - times: A list of directed edges [u, v, w], where w is the travel time from u to v.
# - n: Total number of nodes.
# - k: The node that initially sends a signal.
# All edge weights are positive.

# Return the minimum time required for every node to receive the signal.

# If any node cannot receive the signal, return -1.

# Example
times = [
    [2, 1, 1],
    [2, 3, 1],
    [3, 4, 1]
]

n = 4
k = 2

#      1
#      ↑
#    1 |
#      2 ───1──→ 3 ───1──→ 4

# The signal starts at node 2.

# Shortest travel times:

# Node	Minimum time
# 1	        1
# 2	        0
# 3	        1
# 4	        2

# The last node receives the signal after 2 time units.
# Expected output: 2

def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    # Your implementation
    pass