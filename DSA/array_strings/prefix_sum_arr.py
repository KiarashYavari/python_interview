# ✅ What is Prefix Sum?

# A prefix sum is a technique where we preprocess an array so that:

# We can answer range sum queries in O(1) time.

# Instead of calculating the sum every time from scratch, we store cumulative sums.

# 🔢 Basic Idea

# Given an array:

# nums = [2, 4, 1, 7, 3]

# We build a new array prefix where:

# prefix[i] = sum of elements from index 0 to i

# So:

# prefix[0] = 2
# prefix[1] = 2 + 4 = 6
# prefix[2] = 6 + 1 = 7
# prefix[3] = 7 + 7 = 14
# prefix[4] = 14 + 3 = 17

# Final prefix array:

# [2, 6, 7, 14, 17]
# 🚀 Why Is This Powerful?

# Now imagine the interviewer asks:

# What is the sum of elements from index 1 to index 3?

# Without prefix sum:

# 4 + 1 + 7 = O(n)

# With prefix sum:

# sum(1 → 3) = prefix[3] - prefix[0]
#             = 14 - 2
#             = 12

# 🔥 Range sum becomes:

# sum(L → R) = prefix[R] - prefix[L - 1]

# If L = 0:

# sum(0 → R) = prefix[R]

# Time complexity per query: O(1)
# Preprocessing cost: O(n)

# 🧠 When Do We Use Prefix Sum?

# Use it when:

# 1️⃣ Multiple range sum queries

# If you must compute many:

# sum(i, j)

# sum(l, r)

# sum(a, b)

# Instead of recalculating each time → build prefix once.

# 2️⃣ Subarray problems

# Very common interview pattern:

# Find subarrays with sum = k
# Find number of subarrays with sum divisible by k
# Find longest subarray with equal 0s and 1s

# Prefix sum + HashMap = 🔥 Interview gold.

# 3️⃣ Detecting patterns in cumulative data

# Like:

# Running totals

# Financial analysis

# Traffic accumulation

# Energy usage tracking

# 🌎 Real-World Examples

# Let’s connect this to real life (important for interviews).

# 🏦 1. Bank Transactions

# You have daily transactions:

# [+100, -50, +200, -20, +70]

# If someone asks:

# What was my net income from day 2 to day 4?

# Prefix sum gives instant answer.

# This is literally how financial dashboards optimize performance.

# 📊 2. Website Traffic Analytics

# Daily visitors:

# [1000, 1200, 900, 1500, 1800]

# Marketing asks:

# How many users visited between March 2 and March 4?

# Prefix sum avoids recalculating sums every time.

# 🎮 3. Game Score Tracking

# Player gains points each round.

# Want:

# Total score between level 10–20

# Fast leaderboard stats

# Prefix sum makes it instant.

# 🛒 4. E-commerce Sales Dashboard

# Daily sales:

# [5000, 7000, 6500, 8000, 9000]

# CEO asks:

# Total revenue last week?

# You don’t loop every time — you precompute cumulative revenue.

# 💻 Basic Implementation
def build_prefix(nums):
    prefix = [0] * len(nums)
    prefix[0] = nums[0]

    for i in range(1, len(nums)):
        prefix[i] = prefix[i - 1] + nums[i]

    return prefix

# Range sum:

def range_sum(prefix, left, right):
    if left == 0:
        return prefix[right]
    return prefix[right] - prefix[left - 1]


# 🎯 Advanced Interview Pattern

# Now we level up.

# Instead of storing prefix in array only, we sometimes:

# prefix_sum += nums[i]

# And store frequencies in a hash map.

# Example:

# Count subarrays with sum = k

# This uses:

# if prefix_sum - k exists in hashmap:
#     count += frequency

# 🎯 The Advanced Pattern: Prefix Sum + HashMap

# We are solving:

# Count the number of subarrays whose sum equals k

# Classic problem: Subarray Sum Equals K.

# 🧠 First, Understand the Brute Force

# Given:

# nums = [1, 2, 3]
# k = 3

# All subarrays:

# [1] = 1
# [1,2] = 3 ✅
# [1,2,3] = 6
# [2] = 2
# [2,3] = 5
# [3] = 3 ✅

# Answer = 2

# Brute force:

# Fix start

# Expand end

# Calculate sum each time

# Time complexity = O(n²)

# We need better.

# 🚀 Key Insight (The Magic Idea)

# Let:

# prefix[i] = sum from index 0 → i

# Suppose we are at index i.

# Current prefix sum:

# current_sum = prefix[i]

# We want a subarray that ends at i and sums to k.

# That means:

# prefix[i] - prefix[j] = k

# Rearrange:

# prefix[j] = prefix[i] - k

# 🔥 Translation:

# If we have seen a prefix sum equal to (current_sum - k) before,
# then we found a valid subarray.

# 🧮 Why This Works (Intuition)

# Imagine cumulative sums like this:

# Index:   0   1   2   3
# nums:    1   2   1   2
# prefix:  1   3   4   6

# Let’s say:

# k = 3

# At index 1:

# current_sum = 3
# current_sum - k = 0

# Have we seen 0 before?

# 👉 Yes — before starting (important trick!)

# So subarray [0..1] = 3

# 🔥 The Critical Trick

# We initialize:

# prefix_count = {0: 1}

# Why?

# Because:

# A subarray starting from index 0

# With sum = k

# Needs prefix[i] - k = 0

# Without this, you miss those cases.

# 🧩 Full Example (Step-by-Step)
# nums = [1, 1, 1]
# k = 2

# Expected answer = 2

# Subarrays:

# [1,1] (index 0-1)
# [1,1] (index 1-2)
# Step Through It

# Initialize:

# prefix_sum = 0
# count = 0
# prefix_count = {0:1}
# i = 0
# prefix_sum = 1
# prefix_sum - k = 1 - 2 = -1

# Not in hashmap.

# Add prefix_sum:

# prefix_count = {0:1, 1:1}
# i = 1
# prefix_sum = 2
# prefix_sum - k = 2 - 2 = 0

# 0 exists in hashmap (frequency = 1)

# So:

# count += 1

# Now:

# count = 1

# Add prefix_sum:

# prefix_count = {0:1, 1:1, 2:1}
# i = 2
# prefix_sum = 3
# prefix_sum - k = 3 - 2 = 1

# 1 exists in hashmap (frequency = 1)

# So:

# count += 1

# Final:

# count = 2

# Correct.

"""
    🧠 Why Frequency Matters

    Consider:

    nums = [1, -1, 1, -1, 1]
    k = 0

    Prefix sums:

    1, 0, 1, 0, 1

    Notice:
    0 appears multiple times.

    Each repeated prefix sum means:
    There are multiple subarrays summing to 0.

    That’s why we store frequency, not just existence.
"""
# 💻 Final Clean Implementation
def subarray_sum(nums, k):
    prefix_sum = 0
    count = 0
    prefix_count = {0: 1}

    for num in nums:
        prefix_sum += num

        if prefix_sum - k in prefix_count:
            count += prefix_count[prefix_sum - k]

        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

    return count

# ⏱ Time & Space Complexity
# Metric	Value
# Time	O(n)
# Space	O(n)

# Because:

# One pass through array

# HashMap operations are O(1)

# 🌎 Real-World Analogy

# Imagine:

# You track cumulative money earned each day.

# You want:

# How many continuous time periods earned exactly $10,000?

# Instead of recalculating every interval,
# you track running total and store past totals.

# Whenever:

# current_total - 10000

# was seen before → you found a valid period.

# Financial analytics systems use this exact logic.


# 🔥 Why Interviewers Love This Pattern

# It tests:

# Mathematical transformation skill

# Ability to reduce O(n²) → O(n)

# Hash map mastery

# Prefix logic understanding

# Edge case awareness (like negative numbers)


# ⚠️ Important Notes
# This works even with negative numbers.

# Sliding window DOES NOT work if negatives exist.
# Prefix + hashmap DOES.


# 🎯 Variations Built on This Pattern

# If you master this, you can solve:

# Count subarrays with sum divisible by k

# Longest subarray with sum = k

# Count subarrays with equal 0 and 1

# Continuous Subarray Sum

# Binary Subarrays With Sum

# All same pattern. Only small modification.

"""
    🧪 Assessment Question — Prefix Sum
    Problem: Count Subarrays With Target Sum

    You are given an integer array nums and an integer k.

    Return the total number of continuous subarrays whose sum equals k.

    A subarray is a contiguous part of the array.
"""

"""
    Example 1
    Input:
    nums = [1, 1, 1]
    k = 2

    Output:
    2


    Explanation:

    [1,1] (index 0-1)
    [1,1] (index 1-2)
    
    Example 2
    Input:
    nums = [1, 2, 3]
    k = 3

    Output:
    2


    Explanation:

    [1,2]
    [3]

    Example 3
    Input:
    nums = [3, 4, 7, 2, -3, 1, 4, 2]
    k = 7

    Output:
    4


    Subarrays:

    [3,4]
    [7]
    [7,2,-3,1]
    [1,4,2]

"""

# 📌 Constraints
# 1 ≤ nums.length ≤ 20,000
# -1000 ≤ nums[i] ≤ 1000
# -10^7 ≤ k ≤ 10^7


# Important detail:

# ⚠️ Negative numbers exist, which means:

# ❌ Sliding window will NOT work
# ✅ Prefix Sum + HashMap is required

def count_subarr_to_target(nums: list, k: int) -> int:
    prefix_sum = 0
    prefix_count = {0:1}
    count = 0
    
    for index in range(len(nums)):
        # calculating the sum of arr intgers
        prefix_sum += nums[index]
        if prefix_sum - k in prefix_count:
            # count the subarray that are equal to k
            count += prefix_count[prefix_sum - k]
            
        # frequency arr counting   
        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
        
    # print("prefix_sum: ", prefix_sum)
    # print("prefix_count: ", prefix_count)
    return count
           
print(count_subarr_to_target(nums = [1, 2, 3], k=3))