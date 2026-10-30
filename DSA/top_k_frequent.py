# Top K Frequent Elements
# two concepts: hash tables and heaps.
# Problem: LeetCode 347 — Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements.

# Example 1:
# nums = [1, 1, 1, 2, 2, 3]
# k = 2

# Output: [1, 2]

#Because:
# - 1 appears 3 times.
# - 2 appears 2 times.
# - 3 appears 1 time.

# Example 2:
nums = [4, 4, 5, 5, 5, 6, 6, 6, 6]
k = 2

# Output: [6, 5]

# Use a dictionary to count frequencies and a min-heap of size k to find the most frequent elements.
import heapq

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    frequency = {}

    # Step 1: Count each number's frequency


    heap = []

    # Step 2: Push (frequency, number)
    # into the min-heap
    
    # Step 3: Keep heap size <= k

    # Step 4: Return the numbers
    # from the heap
