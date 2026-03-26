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

# 🔷 What is “Greedy Iteration”?
# 👉 A greedy algorithm means:
# At each step, pick the best immediate (local) choice
# and never go back to change it.
# You iterate through data and lock in decisions on the fly.

# 🔷 Simple Intuition
# Imagine:
# You’re picking items
# At each step, you choose what looks best right now
# You don’t reconsider previous picks
# 👉 No backtracking
# 👉 No trying all combinations
# 👉 Just move forward
# 🔷 Why Sorting is Used with Greedy
# Greedy often works only after sorting, because:
# Sorting creates a meaningful order
# That order guarantees your local decision is safe

# 🔷 Classic Example: Meeting Scheduling
# Problem:
# You have meetings with start/end times.
# 👉 Maximize number of meetings you can attend.

# Greedy Strategy
# 👉 Sort by end time
# 👉 Always pick the meeting that finishes earliest
# Why?
# Because it leaves maximum room for future meetings

intervals.sort(key=lambda x: x[1])  # sort by end time

count = 0
end = float('-inf')

for start, finish in intervals:
    if start >= end:
        count += 1
        end = finish

# Key Insight
# ❌ Don’t pick longest meeting
# ❌ Don’t try all combinations
# ✅ Just pick the earliest finishing one — always

# 🔷 Real-World Examples
# 🗓️ 1. Calendar Scheduling (Google Calendar)
# You want to attend as many meetings as possible
# System chooses:
# 👉 Meetings that end earliest
# Why greedy works:
# Early finish → more room for next events
        
# 💰 2. Making Change (Cash System)
# Problem:
# Return $87 using bills: 50, 20, 10, 5, 1
# Greedy:
# Take largest bill first:
# 50 → remaining 37
# 20 → remaining 17
# 10 → remaining 7
# 5 → remaining 2
# 1 → remaining 0
# 👉 Always pick biggest possible
# ⚠️ Note: Works only for certain currency systems

        
# 📦 3. Shipping / Packing
# You want to fit items into a box
# Strategy:
# 👉 Pick smallest/lightest items first
# OR
# 👉 Pick highest value first
# Used in:
# Logistics
# Warehouse optimization
        
# 🌐 4. Network Routing (Simplified Idea)
# Choose shortest available path step-by-step
# Used in algorithms like:
# 👉 Dijkstra (a form of greedy)
        
# 🎯 5. Job Scheduling for Profit
# Jobs have deadlines + profit
# Strategy:
# 👉 Do highest profit jobs first (after sorting)
# 🔷 When Does Greedy Work?
# Greedy works when:
# ✅ 1. Local choice = global optimum
# Your small decision leads to overall best result
# ✅ 2. Problem has structure (after sorting)
# Sorting makes decisions safe

# 🔴 When Greedy FAILS
# Important for interviews:
# Greedy fails when:
# Future decisions depend on past choices
# You need to explore combinations
# 👉 Example:
# Knapsack (0/1 version) → needs DP, not greedy

# 🔷 How to Recognize Greedy Problems
# Look for phrases like:
# “Maximum number of…”
# “Minimum cost…”
# “Non-overlapping…”
# “Earliest / smallest / largest…”
# “At each step…”
# 👉 Big hint: You can make a decision and never revisit it

# 🔷 Mental Model (Very Important)
# Think:
# “If I choose the best option right now,
# will I regret it later?”
# If NO → greedy works ✅
# If YES → need DP/backtracking ❌

# assessment type greedy technique practice
# 🧠 Problem: Maximum Number of Non-Overlapping Meetings
# 📝 Problem Statement
# You are given a list of meeting time intervals:
# intervals = [[start1, end1], [start2, end2], ...]
# 👉 Return the maximum number of non-overlapping meetings you can attend.
# 📌 Example
# intervals = [[1,3], [2,4], [3,5], [0,6], [5,7]]
# 👉 Output:
# 3
# 🎯 Real-World Context
# Think of:
# 📅 Calendar scheduling (Google Calendar)
# 🧑‍💼 Attending meetings without conflicts
# 🖥️ CPU scheduling tasks

# 🚫 Brute Force Thinking (Wrong Path)
# Try all combinations → O(2ⁿ) 😬
# Not acceptable in interviews
# ✅ Greedy Insight (KEY)
# 👉 Always pick the meeting that ends earliest
# Why?
# It leaves the most room for future meetings.

def max_meetings(intervals: list[list[int]]) -> int:
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[1])
    start = intervals[0][0]
    end = intervals[0][1]
    count = 1
    for index in range(1, len(intervals)):
        if end <= intervals[index][0]:
            count +=1
            end = intervals[index][1]
    
    return count

print(max_meetings([[1,10], [2,3], [4,5], [6,7]]))
#--------------------------------
#--------------------------------

# 🧪 Core Test Cases
# ✅ 1. Basic overlapping
# intervals = [[1,3], [2,4], [3,5], [0,6], [5,7]]
# # Expected: 3
# ✅ 2. No overlaps at all
# intervals = [[1,2], [2,3], [3,4], [4,5]]
# # Expected: 4
# 👉 Tests: end == start allowed
# ❌ 3. All overlapping
# intervals = [[1,5], [2,6], [3,7], [4,8]]
# # Expected: 1
# 👉 Only one can be chosen
# ⚠️ 4. Same end times
# intervals = [[1,4], [2,4], [3,4]]
# # Expected: 1
# 👉 Sorting stability shouldn’t break logic
# ⚠️ 5. Same start times
# intervals = [[1,2], [1,3], [1,4]]
# # Expected: 1
# 👉 Should pick shortest (ends earliest)
# 🧠 6. Unsorted input (IMPORTANT)
# intervals = [[5,7], [1,3], [3,5], [2,4]]
# # Expected: 3
# 👉 Ensures you actually sort
# ⚠️ 7. Nested intervals
# intervals = [[1,10], [2,3], [4,5], [6,7]]
# # Expected: 3
# 👉 Greedy must avoid large interval
# ⚠️ 8. Single interval
# intervals = [[1,2]]
# # Expected: 1
# ⚠️ 9. Empty input
# intervals = []
# # Expected: 0
# ⚠️ 10. Negative times
# intervals = [[-5,-3], [-2,0], [-4,-1]]
# # Expected: 2
# 👉 Tests general robustness
# 🔥 11. Tricky ordering case (INTERVIEW FAVORITE)
# intervals = [[1,4], [2,3], [3,5]]
# # Expected: 2
# 👉 Correct pick:
# [2,3]
# [3,5]
# ❌ Wrong greedy (if sorted by start):
# picks [1,4] → ruins solution
# 🔥 12. Many tiny vs one big
# intervals = [[1,100], [2,3], [3,4], [4,5], [5,6]]
# # Expected: 4
# 👉 Must skip large interval
# ⚠️ 13. Duplicate intervals
# intervals = [[1,3], [1,3], [1,3]]
# # Expected: 1
# 🔥 14. Boundary touching chain
# intervals = [[1,2], [2,3], [3,4], [1,3]]
# # Expected: 3
