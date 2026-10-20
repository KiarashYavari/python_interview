# Exercise: Course Schedule
# LeetCode 207 — Medium

# This is a very common graph interview problem.
# Problem Statement
# You are given an integer numCourses representing the number of courses you must take.
# Courses are labeled:
# 0, 1, 2, ..., numCourses - 1
# You are also given a list of prerequisite pairs:
# [a, b]   This means:

# To take course a, you must first complete course b.
# Return True if you can finish all courses. Otherwise, return False.

# numCourses = 4

# prerequisites = [
#     [1, 0],
#     [2, 1],
#     [3, 2]
# ]
# graph = {0: [1], 1: [2], 2: [3], 3: []}

def can_finish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    # convert prerequisites to adjusency list
    graph = {num : [] for num in range(numCourses) }
    for course, pre in prerequisites:
        graph[pre].append(course)
    # print(graph)
    visited = set()
    path = set()
    def dfs(node):
        # cycle # can't finish all courses
        if node in path:
            return True
        
        # not a cycle # can finish all courses
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
                return False
    return True
        
    
# print(can_finish(numCourses, prerequisites))

# Complexity Analysis
# Let:
# - V = number of courses
# - E = number of prerequisite pairs

# Complexity	Value	    Explanation
# Time	        O(V + E)	Each course and prerequisite edge is explored at most once
# Space	        O(V + E)	Adjacency list, visited/path sets, and recursion stack

# This is the optimal asymptotic complexity for Course Schedule.

# ********************************************************
# ********************************************************

# Exercise: Course Schedule II (LeetCode 210)
# You've now learned how to determine whether a directed graph contains a cycle.

# Let's take that one step further.

# In Course Schedule I, we only returned:
# True  # Can finish all courses
# False # Cannot finish all courses

# But what if the interviewer asks:
# "In what order should the student take the courses?"
# That's where Topological Sorting comes in.

# Topological sorting:

# Problem Statement
# Given numCourses and prerequisites, return a valid ordering of all courses.
# If completing all courses is impossible, return an empty list.

# Example
# numCourses = 4

# prerequisites = [
#     [1, 0],
#     [2, 0],
#     [3, 1],
#     [3, 2]
# ]

#    0
#   / \
#  v   v
#  1   2
#   \ /
#    v
#    3

# Possible valid outputs: [0, 1, 2, 3] or [0, 2, 1, 3] 
# Both are valid because course 3 requires completing both 1 and 2.

def find_order(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    # Your implementation
    pass