# Kadane’s Algorithm (Maximum Subarray)

# Kadane’s Algorithm is a classic technique used to solve the Maximum Subarray Problem in O(n) time.

# The problem:

# Given an integer array nums, find the contiguous subarray with the largest sum and return that sum.

# Example:

# nums = [-2,1,-3,4,-1,2,1,-5,4]

# Output = 6

# Because the best subarray is:

# [4, -1, 2, 1] = 6

# Core Idea (Interview Intuition)

# At every index we decide:

# Should we extend the current subarray or start a new one?

# We track two values:

# current_sum  → best subarray ending at this index
# max_sum      → best subarray found so far

# Decision rule:

# current_sum = max(num, current_sum + num)

# Meaning:

# Either start fresh at this element

# Or extend the previous subarray

"""
    Array:

    [-2,1,-3,4,-1,2,1,-5,4]
    num	current_sum	max_sum
    -2	-2	-2
    1	1	1
    -3	-2	1
    4	4	4
    -1	3	4
    2	5	5
    1	6	6
    -5	1	6
    4	5	6

    Final answer:

    max_sum = 6
"""

# Python Implementation
def max_subarray(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Time Complexity:

# O(n)

# Space Complexity:

# O(1)

# This is optimal.

"""
    1️⃣ The Core Pattern Behind Kadane

    Kadane is used when a problem asks for:

    Maximum or minimum value of a contiguous subarray.

    The keyword is contiguous.

    Typical phrases you will see:

    maximum subarray

    largest sum of consecutive elements

    best continuous segment

    maximum profit segment

    maximum score from consecutive values

    2️⃣ The Mathematical Structure

    Kadane works because the optimal answer follows this recurrence:

    f(i) = \max(nums[i],; nums[i] + f(i-1))

    Meaning:

    At index i:

    Start a new subarray

    Or extend the previous one

    If a problem naturally fits this extend-or-restart decision, Kadane is the solution.

    3️⃣ Quick Recognition Checklist (Interview Trick)

    Ask yourself these 3 questions:

    ✅ 1. Are we dealing with a contiguous subarray?

    Example:

    maximum sum of a contiguous subarray

    ✔ Kadane candidate.

    ✅ 2. Do we want a maximum or minimum total value?

    Example:

    maximum score
    maximum profit
    maximum sum
    minimum cost

    ✔ Kadane candidate.

    ✅ 3. Can the answer be built incrementally while scanning once?

    Meaning:

    You only need information from the previous step.

    ✔ Kadane candidate.
"""

# 4️⃣ When NOT to Use Kadane

# Recognizing when not to use it is equally important.

# ❌ If the subarray is NOT contiguous

# Example:

# pick elements with maximum sum

# You could pick any elements → not Kadane.

# ❌ If there is a fixed window size

# Example:

# maximum sum of subarray of size k

# Use Sliding Window instead.

# ❌ If the problem involves cumulative ranges

# Example:

# sum of subarray between i and j

# Use Prefix Sum.

# 5️⃣ Pattern Comparison (Very Important)
# Pattern	Typical Question	Technique
# contiguous maximum/minimum	maximum subarray	Kadane
# fixed window	max sum of k elements	Sliding Window
# range sums	sum between i and j	Prefix Sum
# pair search	two numbers sum to target	Two Pointers / HashMap
# 6️⃣ Classic Problems Where Kadane Appears

# You should immediately recognize it in these:

# 1️⃣ Maximum Subarray (LeetCode 53)

# 2️⃣ Maximum Circular Subarray

# 3️⃣ Maximum Product Subarray

# 4️⃣ Maximum Sum Rectangle in Matrix (2D Kadane)

# 5️⃣ Stock Profit variants