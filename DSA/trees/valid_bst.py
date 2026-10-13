# Problem statement
# Given the root of a binary tree, determine whether it is a valid Binary Search Tree.
# Remember that for every node:
# - All values in its left subtree must be smaller.
# - All values in its right subtree must be greater.
# - Both subtrees must also satisfy the BST property.
# example- Valid BST:
  #     8
  #    / \
  #   3   10
  #  / \
  # 1   6
# output: True
# Example 2: Invalid BST
#   8
#  / \
# 3   10
#    /
#   5
# output: False
def is_valid_bst(root):

    def dfs(node, lower, upper):
        if node is None:
            return True

        # Check whether node.val is within bounds

        # Recursively validate left subtree
        # with updated upper bound

        # Recursively validate right subtree
        # with updated lower bound

        # Return True only if both are valid

    return dfs(root, float("-inf"), float("inf"))
