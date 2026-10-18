# Number of Islands
# LeetCode 200 — Medium
# This is one of the most common graph interview problems.
# It combines everything we've practiced:
# - Graph traversal
# - DFS
# - Connected components
# - Visited tracking
# - 2D arrays
#*********************************
#*********************************
# Problem Statement
# You are given an m × n 2D grid containing:
# - "1" representing land
# - "0" representing water
# An island is formed by connecting adjacent lands horizontally or vertically.
# Diagonal connections do not count.
# Return the total number of islands.
# Example:
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
grid2 = [
    ["1", "0", "1"],
    ["1", "1", "1"],
    ["0", "0", "1"]
]
# Expected output: 3

def num_islands(grid: list[list[str]]) -> int:
    count = 0
    visited = set()
    m = len(grid) # row num
    n = len(grid[0]) # col num
    def dfs(row, column):
        if row < 0 or column < 0 or row >= m or column >= n:
            return
        
        if (row, column) in visited:
            return
        
        if grid[row][column] == "0":
            return
        
        visited.add((row, column))
        # Explore four directions
        dfs(row - 1, column)  # Up
        dfs(row + 1, column)  # Down
        dfs(row, column - 1)  # Left
        dfs(row, column + 1)  # Right
                
    for row in range(m):
        for col in range(n):
            if (row, col) not in visited and grid[row][col] == "1":
                dfs(row, col)
                count += 1
    return count

print(num_islands(grid2))

# Complexity	Value	    Explanation
# Time	        O(m × n)	Each cell is checked, and each land cell is explored at most once
# Space	        O(m × n)	Visited set and worst-case recursion stack       