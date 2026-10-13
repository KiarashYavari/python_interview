class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
      
root = TreeNode(8)

root.left = TreeNode(3)
root.right = TreeNode(10)

root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
#     8
#    / \
#   3   10
#  / \
# 1   6
def kth_smallest(root, k):
    # Your implementation
    result = []
    def inorder_dfs(node):
      if node is None:
        return None
      inorder_dfs(node.left)
      result.append(node.val)
      inorder_dfs(node.right)
    inorder_dfs(root)
    if k < len(result)+1:
      return result[k-1]
    return None

print(kth_smallest(root, 1))
# Complexity
# Metric	Your solution
# Time	    O(n)
# Space	    O(n + h) = O(n)

# Here, n is the number of nodes and h is the tree height.
# We use O(n) space for the result list and O(h) for the recursive call stack.
#--------------------------------------------------------------------------
#--------optimized solution with while and explicit stack -----------------
def kth_smallest(root, k):
    stack = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        k -= 1

        if k == 0:
            return current.val

        current = current.right

    return None
    
# Complexity:
# - Time: O(h + k) — we can stop after visiting the kth smallest element.
# - Space: O(h) — the stack holds at most a tree-height-dependent number of nodes.
