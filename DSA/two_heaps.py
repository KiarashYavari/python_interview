# Problem: LeetCode 295
# Design a data structure that supports:
# - addNum(num): Add a number.
# - findMedian(): Return the median of all inserted numbers.
# The median is the middle value of a sorted collection.

# For an even number of elements, it's the average of the two middle values.

# How do two heaps solve this?
# We maintain:
# 1. Max-heap (small): Stores the smaller half of the numbers.
# 2. Min-heap (large): Stores the larger half of the numbers.

# Example:
# [6,3,2,4,5,1]
# small = [3, 2, 1]  # Max-heap
# large = [4, 5, 6]  # Min-heap

# median = (3 + 4) / 2  # 3.5

# Implement MedianFinder
# We need two methods:
# - addNum(num) — Insert a number and rebalance the heaps.
# - findMedian() — Return the median.

import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # Max-heap (negative values)
        self.large = []  # Min-heap

    def addNum(self, num: int) -> None:
        # Step 1: Insert into the appropriate heap

        # Step 2: Ensure max(small) <= min(large)

        # Step 3: Balance heap sizes


    def findMedian(self) -> float:
        # If one heap has more elements,
        # return its root

        # Otherwise, return average of both roots

