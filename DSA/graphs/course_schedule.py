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