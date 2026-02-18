# 🔹 What Is the Two-Pointer Technique?

# The **two-pointer technique** is a problem-solving pattern where you use **two indices (pointers)** to iterate through an array or string — usually from:

# * Opposite ends (`left` & `right`)
# * Or same direction but at different speeds

# Instead of nested loops (**O(n²)**), you often reduce it to **O(n)**.

# ---

# 🔹 When Do We Use Two Pointers?

# Use it when:

### 1️⃣ Array is sorted

# You can shrink or expand a range intelligently.

### 2️⃣ You need to find pairs

# Especially:

# * Two numbers that sum to a target
# * Remove duplicates
# * Partition array
# * Reverse something in-place

### 3️⃣ You need in-place modification

# Common in interviews.

# ---

# 🔹 Real World Analogy

# Imagine:

# You’re looking for **two people in a sorted line whose total height equals 300cm**.

# Instead of checking every pair:

# * Start one pointer at shortest
# * One at tallest
# * If sum too big → move tallest down
# * If sum too small → move shortest up

# You eliminate possibilities smartly.

# That’s two pointers.

# ---

# 🔹 Classic Example 1: Two Sum (Sorted Array)

### Problem:

# Given a **sorted** array, find two numbers that sum to target.

# ```
# nums = [1,2,4,6,10]
# target = 8
# ```

# ---

### ❌ Brute Force

# Check every pair → O(n²)

# ---

### ✅ Two Pointer Approach

def two_sum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left, right]

        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []

### Why It Works

# Because the array is sorted:

# * If sum is too small → move left forward
# * If sum is too big → move right backward

# Time complexity: **O(n)**
# Space complexity: **O(1)**

# ---

# 🔹 Classic Example 2: Reverse String (In-place)

s = ["h","e","l","l","o"]

# Use two pointers:


def reverse_string(s):
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


# s = ["o","l", "l", "e", "h"]

# 🔹 Classic Example 3: Remove Duplicates (Sorted Array)

nums = [1,1,2,2,3]


# We keep one pointer for:

# * Position to insert unique number

# And one pointer for:

# * Iteration


def remove_duplicates(nums):
    slow = 0

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1

# This is a variation called **fast & slow pointers**.



# 🔹 Types of Two Pointer Patterns

### 1️⃣ Opposite Direction

# * Two Sum (sorted)
# * Container with most water
# * Palindrome check

### 2️⃣ Same Direction (Fast & Slow)

# * Remove duplicates
# * Move zeros
# * Linked list cycle detection

### 3️⃣ Partition Style

# * Dutch National Flag
# * QuickSort partition


# 🔹 How To Recognize Two-Pointer Problems in Interviews

# If you see:

# * Sorted array
# * Pair problems
# * In-place modification
# * Palindrome
# * Removing duplicates
# * Partitioning

# 👉 Think: "Can I solve this with two pointers?"



# 🔥 Interview-Level Example

### Valid Palindrome


"A man, a plan, a canal: Panama"


# Ignore non-alphanumeric characters.


def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

# # Time: O(n)
# Space: O(1)


# 🚀 Why This Is Powerful in Assessments

# In online assessments (like Walmart-style tests), you often need:

# * Clean logic
# * Linear time
# * Minimal memory

# Two pointers solves many medium problems efficiently.



# 🧠 Your Turn (Practice)

# Try solving:

# 1️⃣ Move all zeros to end (in-place)
# 2️⃣ Check if array is palindrome
# 3️⃣ Find pair with target in sorted array
# -----------------------------------------
"""🧪 Assessment Simulation – Two Pointers
    🧩 Problem: Closest Pair to Target

    You are given a sorted integer array nums and an integer target.

    Return the pair of numbers whose sum is closest to the target.

    If multiple pairs are equally close, return the one with the smallest left index.

    You must:

    Use O(n) time

    Use O(1) extra space
"""
# examples:
# 1
# nums = [1, 3, 4, 7, 10]
# target = 15
# output --> (4, 10)
# Explanation:

# 4 + 10 = 14 (difference = 1)

# 7 + 10 = 17 (difference = 2)

# 3 + 10 = 13 (difference = 2)

# Closest is (4,10)

# 2
# nums = [2, 5, 6, 8, 9]
# target = 14
# output --> (5, 9)

"""🚨 Constraints

    2 ≤ len(nums) ≤ 10⁵

    -10⁴ ≤ nums[i] ≤ 10⁴

    Array is sorted ascending
"""

def closest_pair(nums: list, target: int) -> list:
    left = 0
    right = len(nums) - 1
    best_diff = float("inf")
    best_pair = None
    while left < right:
        current_sum = nums[left] + nums[right]
        current_diff = abs(current_sum - target)
        
        if current_diff < best_diff:
            best_diff = current_diff
            best_pair = [nums[left], nums[right]]
            
        elif current_diff == best_diff:
            if nums[left] < best_pair[0]:
                best_pair = [nums[left], nums[right]]
                
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else: # difference is 0
            return [nums[left], nums[right]]
    return best_pair            

nums = [1, 3, 4, 7, 10]
target = 15
print(closest_pair(nums = nums, target = target))