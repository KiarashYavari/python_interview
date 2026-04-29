# 🪟 What Is the Sliding Window Technique?

# Sliding window is a pattern used to solve problems involving:

# Contiguous subarrays

# Substrings

# Sequential data

# Instead of recomputing results for every possible subarray (O(n²)),
# we maintain a "window" range and slide it efficiently across the array in O(n).

# It is essentially:

# Two pointers + dynamic window resizing.

# 🧠 Core Idea

# You maintain:
# left = 0
# for right in range(n):
#     # expand window by moving right
    
#     while window_is_invalid:
#         # shrink window
#         left += 1

# The window is always:
# nums[left:right+1]
"""
    📌 When Do We Use Sliding Window?

    Use it when the problem mentions:

    ✅ 1. Contiguous elements

    “subarray”

    “substring”

    “continuous segment”

    ✅ 2. Conditions like:

    Longest

    Shortest

    At most K

    Exactly K

    Maximum sum

    Minimum length

    Without repeating characters
"""
#--------
# 🔥 Two Main Types of Sliding Window
# 1️⃣ Fixed-Size Window

# Window size is constant.

# Example:

# Find maximum sum of subarray of size k.

# Example
def max_sum(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum
# Time complexity: O(n)
# Without sliding window: O(n*k)

# 🏪 Real World Example

# Imagine:

# You are analyzing website traffic.

# You want:

# Maximum visitors in any 7 consecutive days.

# Instead of summing every 7-day block from scratch,
# you slide the 7-day window forward.

# 2️⃣ Variable-Size Window (Most Important)

# Window grows and shrinks dynamically.

# Used when condition depends on content.

# 🧠 Classic Example: Longest Substring Without Repeating Characters

# Given:
"abcabcbb"
# Find longest substring without duplicates.

# solution
def lengthOfLongestSubstring(s):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


# 🏪 Real World Example

# Imagine:

# You're building a rate limiter for API calls.

# You want:

# Longest sequence of requests without repeating user IDs.

# You maintain a dynamic window of unique users.
#---------

# 📊 Another Important Pattern
# Smallest Subarray with Sum ≥ Target

# This is very common in interviews.

def min_subarray_len(target, nums):
    left = 0
    total = 0
    min_len = float("inf")

    for right in range(len(nums)):
        total += nums[right]

        while total >= target:
            min_len = min(min_len, right - left + 1)
            total -= nums[left]
            left += 1

    return 0 if min_len == float("inf") else min_len

# 🏪 Real World Example

# Suppose:

# You are analyzing CPU load metrics.

# You want:

# The shortest continuous time interval where CPU usage exceeded threshold.

# Sliding window is perfect.

"""
    🧩 Mental Model (Very Important)

    Think of it like:

    Expand → Expand → Expand → Violates condition
    Shrink → Shrink → Valid again
    Expand again
"""
#-------
# 🔥 Why It's So Powerful

# Instead of:

# Check all subarrays → O(n²)
# You do:

# Each element visited at most twice → O(n)

# Because:

# Right pointer moves n times

# Left pointer moves at most n times

# Total: 2n → O(n)

"""
    ⚠️ When NOT To Use Sliding Window

    Do NOT use it when:

    Subarray does NOT need to be contiguous

    Order does not matter

    Problem involves combinations/subsets

    Then you might need:

    DP

    Backtracking

    Greedy

    Prefix sums

    Binary search
"""

# 🎯 How To Identify Sliding Window in Interview

# If you see:

# “Longest substring…”

# “Shortest subarray…”

# “At most K distinct…”

# “Exactly K…”

# “Without repeating…”

# 🚨 90% chance it’s sliding window.


"""
    🧪 Assessment Problem — Sliding Window (Medium)
    🔐 API Rate Limiter

    You are building a rate limiter for an API service.

    You are given:

    An integer k → maximum allowed requests

    An integer window → time window in seconds

    A sorted list timestamps → request times in seconds

    📌 Rule:

    At any moment, there must be at most k requests within any window seconds.
"""
# 🎯 Task

# Return True if the request pattern is valid.
# Return False if at any time more than k requests occur within a 
# window-second interval.

# 📥 Example 1
k = 3
window = 5
timestamps = [1, 2, 3, 6, 7]
# return True
# Explanation:

# Requests at 1,2,3 → 3 requests in 3 seconds (OK)

# Next window starts naturally

# Never exceeds 3 in 5 seconds

# 📥 Example 2
k = 3
window = 5
timestamps = [1, 2, 3, 4]
# ❌ Output: False
# Explanation:

# From time 1 to 4 → 4 requests within 5 seconds

# Limit exceeded
# -----
# ⛔ Constraints (Assessment Style)

# 1 ≤ len(timestamps) ≤ 10^5

# timestamps sorted ascending

# O(n) expected

# O(1) or O(n) space allowed

# tips:
# 🧠 Think Before Coding
# Take 10–15 minutes and implement it.

def rate_limit_check(k: int, window: int, timestamps: list[int]) -> bool:
    left = 0

    for right in range(len(timestamps)):
        # shrink window if outside allowed time
        while timestamps[right] - timestamps[left] >= window:
            left += 1

        # number of requests in current window
        if right - left + 1 > k:
            return False

    return True

print(rate_limit_check(k = 3, window = 5, timestamps = [1, 4, 5, 6]))
