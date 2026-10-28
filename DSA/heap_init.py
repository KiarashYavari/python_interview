# What is a Heap?
# A heap is a tree-based data structure that lets us efficiently access the smallest or largest element.
# Important: A heap is not a fully sorted tree. It only guarantees that each parent has the correct ordering relative to its children.

# min heap >>> smallest node value is the root or top
# max heap >>> largest node value is the root or top

# Heap operations in Python:
# Python provides heapq, which implements a min-heap.
import heapq

heap = []

# Insert elements
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)
heapq.heappush(heap, 1)

print(heap[0])           # 1 (smallest)
print(heapq.heappop(heap))  # 1
print(heap[0])           # 2

# Operation	                Time complexity
# Peek minimum heap[0]	      O(1)
# Insert heappush()	          O(log n)
# Remove minimum heappop()	  O(log n)
# Convert list heapify()	    O(n)

# For a max-heap, a common interview technique is to store negative numbers:
nums = [3, 1, 7, 4]

max_heap = [-num for num in nums]
heapq.heapify(max_heap)

print(-heapq.heappop(max_heap))  # 7
# ----------------------------------
# ----------------------------------
# Problem: Kth Largest Element in an Array (LeetCode 215)

# Given an integer array nums and an integer k, return the kth largest element.
# Example
nums = [3, 2, 1, 5, 6, 4]
k = 2

# Output: 5
# task: Solve this using a min-heap of size k, without sorting the entire array.
import heapq
import heapq

def find_kth_largest(nums: list[int], k: int) -> int:
    heap = []

    for num in nums:
        # Push num into heap
        heapq.heappush(heap, num)
        # If heap has more than k elements,
        if len(heap) > k:
        # remove the smallest
          heapq.heappop(heap)

    # Return kth largest
    return heap[0]

# print(find_kth_largest(nums, k))
  
