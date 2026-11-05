# Problem: K Closest Points to Origin
# Given an array points, where points[i] = [x, y] represents a point on a 2D plane, and an integer k, return the k points closest to the origin (0, 0).

# The distance between two points is calculated using Euclidean distance:

# d=sqrt{x^2+y^2}


# You may return the answer in any order.

# Example 1
# Input:
# points = [[1, 3], [-2, 2]]
# k = 1
# expected output: [[-2, 2]]

# Example 2
# Input: 
points = [[3, 3], [5, -1], [-2, 4]]
k = 2
# expected output: [[3, 3], [-2, 4]]

import heapq

def k_closest(points: list[list[int]], k: int) -> list[list[int]]:

    # take a heap 
    # iterate over points and get x, y
    heap = []
    for point in points:
      x, y = point
      # push them into heap, use distance comparison
      distance = (x*x) + (y*y)
      heapq.heappush(heap, (distance,x,y))

    # take a result list
    result = []
    # while result lenght is less than k
    while len(result) < k:
      distance,x,y = heapq.heappop(heap)
      # pop from heap and push into results
      result.append([x,y])
      
    return result

# print(k_closest(points, k))

