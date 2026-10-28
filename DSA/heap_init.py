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
