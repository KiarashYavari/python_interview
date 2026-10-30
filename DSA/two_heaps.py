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
        # Step 1: Insert into small
        heapq.heappush(self.small, -num)

        # Step 2: Move largest from small to large
        value = -heapq.heappop(self.small)
        heapq.heappush(self.large, value)

        # Step 3: Balance sizes
        if len(self.large) > len(self.small) + 1:
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]

        return (-self.small[0] + self.large[0]) / 2


m_finder = MedianFinder()

for num in range(1, 6):
    m_finder.addNum(num)
    print(f"add {num}")
    print("small:", m_finder.small)
    print("large:", m_finder.large)

print("Median:", m_finder.findMedian())
