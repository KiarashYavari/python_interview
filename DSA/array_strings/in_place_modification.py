# ============================================================
# Arrays & Strings - In-place Modification
# ============================================================

"""
What Is In-place Modification?

In-place modification means changing the original array/list directly
instead of creating a new array.

In interviews, this usually means:

- Modify nums directly
- Use O(1) extra space
- Return the new length, count, or modified array
- Do not create another list unless allowed

Common interview signals:

- "Modify the array in-place"
- "Use O(1) extra space"
- "Return the new length"
- "Move all zeros to the end"
- "Remove duplicates"
- "Remove all occurrences of val"
- "Reverse the string in-place"
"""

# ============================================================
# Pattern 1: Remove Element
# ============================================================

"""
Problem:
Given nums and val, remove all occurrences of val in-place.
Return the new length.

Example:
nums = [3, 2, 2, 3]
val = 3

Output:
2

Modified nums starts with:
[2, 2]
"""


def remove_element(nums: list[int], val: int) -> int:
    write = 0

    for read in range(len(nums)):
        if nums[read] != val:
            nums[write] = nums[read]
            write += 1

    return write


# ============================================================
# Pattern 2: Move Zeroes
# ============================================================

"""
Problem:
Move all zeroes to the end while keeping the order of non-zero elements.

Example:
nums = [0, 1, 0, 3, 12]

Output:
[1, 3, 12, 0, 0]
"""


def move_zeroes(nums: list[int]) -> None:
    write = 0

    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1

    while write < len(nums):
        nums[write] = 0
        write += 1


# ============================================================
# Pattern 3: Remove Duplicates from Sorted Array
# ============================================================

"""
Problem:
Given a sorted array, remove duplicates in-place.
Return the number of unique elements.

Example:
nums = [1, 1, 2, 2, 3]

Output:
3

Modified nums starts with:
[1, 2, 3]
"""


def remove_duplicates(nums: list[int]) -> int:
    if not nums:
        return 0

    write = 1

    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1

    return write


# ============================================================
# Pattern 4: Reverse String In-place
# ============================================================

"""
Problem:
Reverse a list of characters in-place.

Example:
s = ["h", "e", "l", "l", "o"]

Output:
["o", "l", "l", "e", "h"]
"""


def reverse_string(s: list[str]) -> None:
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


# ============================================================
# Pattern 5: Sort Colors
# ============================================================

"""
Problem:
Given an array with only 0, 1, and 2, sort it in-place.

Example:
nums = [2, 0, 2, 1, 1, 0]

Output:
[0, 0, 1, 1, 2, 2]

This is also called the Dutch National Flag problem.
"""


def sort_colors(nums: list[int]) -> None:
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1

        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


# ============================================================
# Pattern 6: String Compression
# ============================================================

"""
Problem:
Compress repeated characters in-place.

Example:
chars = ["a", "a", "b", "b", "c", "c", "c"]

Output:
6

Modified chars starts with:
["a", "2", "b", "2", "c", "3"]
"""


def compress(chars: list[str]) -> int:
    write = 0
    read = 0

    while read < len(chars):
        current_char = chars[read]
        count = 0

        while read < len(chars) and chars[read] == current_char:
            read += 1
            count += 1

        chars[write] = current_char
        write += 1

        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1

    return write


# ============================================================
# Assessment Simulation
# ============================================================

"""
Problem: Move Target Values to End

You are given an integer array nums and an integer target.

Move all occurrences of target to the end of the array in-place while
keeping the relative order of all non-target values.

Return nums.

You must:
- Modify nums in-place
- Use O(1) extra space
- Use O(n) time

Example 1:
nums = [2, 1, 2, 3, 4, 2]
target = 2

Output:
[1, 3, 4, 2, 2, 2]

Example 2:
nums = [0, 1, 0, 3, 12]
target = 0

Output:
[1, 3, 12, 0, 0]

Example 3:
nums = [1, 2, 3]
target = 4

Output:
[1, 2, 3]
"""


def move_target_to_end(nums: list[int], target: int) -> list[int]:
    write = 0

    for read in range(len(nums)):
        if nums[read] != target:
            nums[write] = nums[read]
            write += 1

    while write < len(nums):
        nums[write] = target
        write += 1

    return nums


# ============================================================
# Test Cases
# ============================================================

if __name__ == "__main__":
    nums1 = [3, 2, 2, 3]
    length1 = remove_element(nums1, 3)
    print("remove_element:", length1, nums1[:length1])
    # Expected: 2 [2, 2]

    nums2 = [0, 1, 0, 3, 12]
    move_zeroes(nums2)
    print("move_zeroes:", nums2)
    # Expected: [1, 3, 12, 0, 0]

    nums3 = [1, 1, 2, 2, 3]
    length3 = remove_duplicates(nums3)
    print("remove_duplicates:", length3, nums3[:length3])
    # Expected: 3 [1, 2, 3]

    chars1 = ["h", "e", "l", "l", "o"]
    reverse_string(chars1)
    print("reverse_string:", chars1)
    # Expected: ["o", "l", "l", "e", "h"]

    nums4 = [2, 0, 2, 1, 1, 0]
    sort_colors(nums4)
    print("sort_colors:", nums4)
    # Expected: [0, 0, 1, 1, 2, 2]

    chars2 = ["a", "a", "b", "b", "c", "c", "c"]
    length2 = compress(chars2)
    print("compress:", length2, chars2[:length2])
    # Expected: 6 ["a", "2", "b", "2", "c", "3"]

    nums5 = [2, 1, 2, 3, 4, 2]
    print("move_target_to_end:", move_target_to_end(nums5, 2))
    # Expected: [1, 3, 4, 2, 2, 2]
