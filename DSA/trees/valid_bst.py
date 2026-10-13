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
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
      
root = TreeNode(8)

root.left = TreeNode(3)
root.right = TreeNode(10)

root.left.left = TreeNode(1)
root.left.right = TreeNode(9)
#     8
#    / \
#   3   10
#  / \
# 1   6
def is_valid_bst(root):

    def dfs(node, lower, upper):
        if node is None:
            return True

        # Check whether node.val is within bounds
        if node.val >= upper or node.val <= lower:
          return False

        # Recursively validate left subtree
        # with updated upper bound
        left_subtree = dfs(node.left, lower, node.val)

        # Recursively validate right subtree
        # with updated lower bound
        right_subtree = dfs(node.right, node.val, upper)

        # Return True only if both are valid
        return (left_subtree and right_subtree)

    return dfs(root, float("-inf"), float("inf"))
  
print(is_valid_bst(root))
