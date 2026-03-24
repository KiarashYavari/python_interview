# Great question — this is one of those “hidden patterns” that interviewers expect you to *recognize*, not just memorize.

# ---

# # 🔷 What are “Sorting + Iteration Tricks”?

# They mean:

# 👉 **Sort the input first → then iterate in a smart way to simplify the problem**

# Instead of brute force (`O(n²)` or worse), sorting lets you:

# * Reduce comparisons
# * Use structure (ordered data)
# * Apply greedy decisions
# * Skip unnecessary work

# ---

# # 🔷 Why Sorting Helps

# When data is sorted:

# * Similar elements are **grouped**
# * Order gives **direction** (small → large)
# * You can **break early**
# * You can **avoid duplicates easily**

# 👉 This often turns:

# * `O(n²)` → `O(n log n)`
# * Or enables patterns like **two pointers**

# ---

# # 🔷 Core Sorting + Iteration Tricks

# ---

# ## 1️⃣ Sort + Skip Duplicates

#

# ### Idea:

# After sorting, duplicates are adjacent → easy to skip

# ### Example Problem:

# * **3Sum**
# * Remove duplicates

# ### Code Pattern:

# ```python
# nums.sort()

# for i in range(len(nums)):
#     if i > 0 and nums[i] == nums[i - 1]:
#         continue  # skip duplicates
# ```

# ### Why it matters:

# Without sorting → duplicate handling is messy
# With sorting → clean and efficient

# ---

# ## 2️⃣ Sort + Two Pointer Scan

# 

# ### Idea:

# Use `left` and `right` pointers on sorted array

# ### Example Problems:

# * Two Sum (sorted)
# * Closest pair
# * 3Sum

# ### Code Pattern:

# ```python
# nums.sort()
# left, right = 0, len(nums) - 1

# while left < right:
#     s = nums[left] + nums[right]
    
#     if s == target:
#         return [nums[left], nums[right]]
#     elif s < target:
#         left += 1
#     else:
#         right -= 1
# ```

# ### Why it works:

# Sorting gives direction:

# * Too small → move left forward
# * Too big → move right backward

# ---

# ## 3️⃣ Sort + Greedy Iteration

# 

# ### Idea:

# Sort based on a key → pick optimal choices step-by-step

# ### Example Problems:

# * Merge intervals
# * Non-overlapping intervals
# * Activity selection

# ### Code Pattern:

# ```python
# intervals.sort(key=lambda x: x[1])  # sort by end time

# count = 0
# end = float('-inf')

# for start, finish in intervals:
#     if start >= end:
#         count += 1
#         end = finish
# ```

# ### Why:

# Sorting ensures you're always making the **best local decision**

# ---

# ## 4️⃣ Sort + Grouping

# 

# ### Idea:

# Sort elements (or keys) → group similar items

# ### Example:

# * Group Anagrams

# ```python
# from collections import defaultdict

# groups = defaultdict(list)

# for word in strs:
#     key = "".join(sorted(word))
#     groups[key].append(word)
# ```

# ### Why:

# Sorted version acts as a **signature**

# ---

# ## 5️⃣ Sort + Binary Search / Positioning

# ### Idea:

# Sort → then efficiently locate positions

# ### Example:

# * Find insertion position
# * Search range

# ```python
# import bisect

# nums.sort()
# pos = bisect.bisect_left(nums, target)
# ```

# ---

# # 🔷 Real-World Example

# ## 🧑‍💼 Scheduling Meetings (VERY common in interviews)

# ### Problem:

# You have meeting time intervals.
# Find maximum non-overlapping meetings.

# ### Why sorting is used:

# * Sort by **end time**
# * Then iterate greedily

# ### Real-world meaning:

# 👉 Calendar apps (Google Calendar, Outlook)
# 👉 Booking systems
# 👉 CPU task scheduling

# ---

# ## 🛒 E-commerce Example

# ### Problem:

# Find pairs of products whose prices sum close to a budget

# ### Approach:

# * Sort prices
# * Use two pointers

# 👉 Used in:

# * Recommendation systems
# * Budget filtering

# ---

# ## 📊 Data Deduplication

# ### Problem:

# Remove duplicate records

# ### Approach:

# * Sort records
# * Iterate and skip duplicates

# 👉 Used in:

# * Log processing
# * Data pipelines (ETL)

# ---

# # 🔷 When Should You Think “Sort First”?

# 💡 Strong signals:

# * “Find pairs / triplets”
# * “Avoid duplicates”
# * “Closest / minimum difference”
# * “Intervals”
# * “Greedy selection”
# * “Rearrange / group”

# 👉 If brute force feels like `O(n²)` → try sorting

# ---

# # 🔷 Mental Model (Interview Gold)

# When you see an array problem:

# Ask yourself:

# 1. **Can sorting simplify relationships?**
# 2. **Will order help me move pointers or make decisions?**
# 3. **Can I reduce comparisons after sorting?**

# ---

# # 🔷 Quick Summary

# | Trick                | Use Case              |
# | -------------------- | --------------------- |
# | Sort + Skip          | Remove duplicates     |
# | Sort + Two Pointers  | Pair/triplet problems |
# | Sort + Greedy        | Intervals, scheduling |
# | Sort + Grouping      | Anagrams, clustering  |
# | Sort + Binary Search | Fast lookup           |

# ---

# If you want, next step I can:
# 👉 Give you **5 real interview problems** (like assessments) specifically on sorting tricks
# 👉 Or review your solution step-by-step like an interviewer
