# 1. What is a Binary Search Tree?
# A Binary Search Tree (BST) is a binary tree that follows a specific ordering rule:
# For every node:
# - Left subtree: All values must be smaller than the current node.
# - Right subtree: All values must be greater than the current node.
# - Both left and right subtrees must also follow these rules.
# example:
#       8
#      / \
#     3   10
#    / \    \
#   1   6    14
#      / \   /
#     4   7 13
# Left subtree:  [3, 1, 6, 4, 7]  → All < 8
# Right subtree: [10, 14, 13]     → All > 8
# Left subtree:  [1]        → All < 3
# Right subtree: [6, 4, 7]  → All > 3
# The same rule applies to every node.
# Important distinction
# Every BST is a binary tree, but not every binary tree is a BST.
# Not a valid BST:
    #   8
    #  / \
    # 3   10
    #    /
    #   5
# Because 5 is in the right subtree of 8, but: 5 < 8
# --------------------------------------
# 2. Why are BSTs useful?
# searching an unsorted array:
# nums = [8, 3, 10, 1, 6, 14, 4, 7, 13]
# Without additional information, we might need to check every element.
# Time complexity: O(n)
# But in a balanced BST, we can eliminate an entire subtree at every step.
#       8
#      / \
#     3   10
#    / \    \
#   1   6    14
#      / \   /
#     4   7 13
# searching for 7:
# Step 1: Start at 8
# 7 < 8 So Go left.
# Step 2: We're at 3
# Go right.
# Step 3: We're at 6.
# Go right.
# Step 4: We're at 7.
# Our path: 8 → 3 → 6 → 7
# We only visited 4 nodes instead of potentially checking all 9.
# Operation	Balanced BST	Worst-case BST
# Search	     O(log n)	        O(n)
# Insert	     O(log n)	        O(n)
# Delete	     O(log n)	        O(n)
# Important: A regular BST does not automatically balance itself.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#     8
#    / \
#   3   10
#  / \
# 1   6
root = TreeNode(8)

root.left = TreeNode(3)
root.right = TreeNode(10)

root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
# Search in a Binary Search Tree
# Problem statement
# Given the root of a Binary Search Tree and an integer val, find the node whose value equals val.
# Return that node if it exists, or None otherwise.
# example:
# val = 6
# output : TreeNode(6)
# Notice that we're returning the node itself, not just its value.
# example:
# val = 15
# ouput: None
def search_bst(root, val):
    # Your implementation
    if root is None:
        return None
    # right subtree
    if root.val < val:
        print("right subtree of",root.val)
        return search_bst(root.right, val)
        
    # left subtree
    elif root.val > val:
        print("left subtree of",root.val)
        return search_bst(root.left, val)
        
    # find a match    
    elif root.val == val:
        print("exact match of",root.val)
        return root

match_node = search_bst(root, 1)
if match_node:
    print(match_node.val)
else:
    print(match_node)
#----------------------------------
# Complexity	    Balanced BST	Skewed BST
# Time	                O(log n)	    O(n)
# Space (recursive)	    O(log n)	    O(n)
# improvements: An iterative solution using a while loop can reduce the auxiliary space complexity to O(1).
