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

# Complexity analysis
# Let n be the number of points.
    
# Operation	            Time
# Push n points	        O(n log n)
# Pop k points	        O(k log n)
# Total	                O(n log n)
# Auxiliary space	    O(n)

# reduce the time to O(n log k):
def k_closest(points: list[list[int]], k: int) -> list[list[int]]:

    # take a  max heap 
    # iterate over points and get x, y
    heap = []
    for point in points:
      x, y = point
      # push them into heap, use distance comparison
      distance = (x*x) + (y*y)
      heapq.heappush(heap, (-distance,x,y))

      # if we exceed k elements remove the largest distance
      if len(heap) > k:
        heapq.heappop(heap)
      
    return [[x,y] for _, x, y in heap]

# Notice two important changes:
# 1. -distance ensures the farthest point is at the top of the heap.
# 2. if len(heap) > k removes that farthest point.

#                     first solution	    Optimized
# Heap size	            Up to n	            Up to k + 1
# Insertion cost	    O(log n)	         O(log k)
# Number of points	    n	                   n
# Total time	        O(n log n)	        O(n log k)
# Auxiliary space	    O(n)	              O(k)
